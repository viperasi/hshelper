# -*- coding: utf-8 -*-
__author__ = 'arthurtsu'

import uuid
from PIL import Image, ImageDraw, ImageFont
from QiniuUtil import uploadQiniu

from models import Card, Share, CardClass
from db import db_session

#保存图片
def saveImage(hero, cards):
    return insertData(toQiniu(drawData(hero, cards)))

#画表格
def drawData(hero, cards):
    im = Image.new('RGB', (400, 600), 0xffffff)
    draw = ImageDraw.Draw(im)
    width, height = im.size
    for i in range(1, 30):
        y = i * 30 + 10
        draw.line(((10, y), (width - 10, y)), fill=(225, 225, 225))

    draw.line(((10, 1), (10, height - 20)), fill=(225, 225, 225))
    draw.line(((width - 10, 1), (width - 10, height - 20)), fill=(225, 225, 225))

    draw.rectangle(((10, 1), (width - 10, 40)), fill=(223, 223, 223))

    cc = CardClass.query.filter(CardClass.classId==hero.cclass).first()
    font = ImageFont.truetype('/Library/Fonts/Songti.ttc', 14)
    fontcolor = (14, 77, 157)
    draw.text((20, 10), hero.name, fill=fontcolor, font=font)
    draw.text((140, 10), cc.name, fill=fontcolor, font=font)

    draw.text((20, 45), "name", fill=fontcolor, font=font)
    draw.text((220, 45), "cost", fill=fontcolor, font=font)
    draw.text((280, 45), "att", fill=fontcolor, font=font)
    draw.text((340, 45), "hp", fill=fontcolor, font=font)
    font = ImageFont.truetype('/Library/Fonts/Songti.ttc', 12)
    fontcolor = (50, 100, 100)
    for index, card in enumerate(cards):
        atk = ''
        health = ''
        if card.atk is not None:
            atk = str(card.atk)
        if card.health is not None:
            health = str(card.health)
        height = 30 * (index + 2) + 15
        fontcolor = (50, 100, 100)
        if card.rarity == '3':
            fontcolor = (0, 112, 221)
        elif card.rarity == '4':
            fontcolor = (163, 53, 238)
        elif card.rarity == '5':
            fontcolor = (255, 104, 16)
        draw.text((20, height), card.name + "*" + str(card.card_num), fill=fontcolor, font=font)
        draw.text((220, height), str(card.cost), fill=fontcolor, font=font)
        draw.text((280, height), atk, fill=fontcolor, font=font)
        draw.text((340, height), health, fill=fontcolor, font=font)
    imgname = 'tmp/' + str(uuid.uuid4()) + '.png'
    im.save(imgname)
    return imgname

#上传七牛
def toQiniu(filename):
    return uploadQiniu(filename)

#生成短连接
def genShortUrl(qiniukey):
    return None

#保存数据
def insertData(qiniukey):
    share = Share.query.filter(Share.share_qiniuurl == qiniukey).first()
    if share is None:
        share = Share(None, qiniukey)
        db_session.add(share)
        db_session.commit()
    return share

def test():
    cards = Card.query.order_by(Card.id)[0: 10]
    for card in cards:
        card.card_num = 1
        card.cost = '2'
        card.atk = '2'
        card.health = '5'
    drawData(cards[0], cards)

if __name__ == '__main__':
    test()