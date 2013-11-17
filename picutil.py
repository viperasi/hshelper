# -*- coding: utf-8 -*-
__author__ = 'arthurtsu'

import uuid
from PIL import Image, ImageDraw, ImageFont
from QiniuUtil import uploadQiniu

from models import Card, Share
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

    font = ImageFont.truetype('/Library/Fonts/Songti.ttc', 14)
    fontcolor = (14, 77, 157)
    draw.text((20, 10), hero.card_name, fill=fontcolor, font=font)
    draw.text((140, 10), hero.card_class, fill=fontcolor, font=font)

    draw.text((20, 45), "name", fill=fontcolor, font=font)
    draw.text((220, 45), "cost", fill=fontcolor, font=font)
    draw.text((280, 45), "att", fill=fontcolor, font=font)
    draw.text((340, 45), "hp", fill=fontcolor, font=font)
    font = ImageFont.truetype('/Library/Fonts/Songti.ttc', 12)
    fontcolor = (50, 100, 100)
    for index, card in enumerate(cards):
        height = 30 * (index + 2) + 15
        draw.text((20, height), card.card_name + "*" + str(card.card_num), fill=fontcolor, font=font)
        draw.text((220, height), card.card_cost, fill=fontcolor, font=font)
        draw.text((280, height), card.card_att, fill=fontcolor, font=font)
        draw.text((340, height), card.card_hp, fill=fontcolor, font=font)
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
        card.card_cost = '2'
        card.card_att = '2'
        card.card_hp = '5'
    drawData(cards[0], cards)

if __name__ == '__main__':
    test()