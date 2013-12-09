# -*- coding: utf-8 -*-
__author__ = 'Arthur.Tsu'

import lxml.etree
import os
from models import Card,CardI18NFlavorText, CardI18NName, CardI18NHowtogold, CardI18NTextinhand
from models import CardClass, CardSet, CardFaction, CardRace, CardRarity, CardType
from db import db_session

XML_DIRECTORY = 'hearthstone-data-1.0.0.3937/xml/TextAsset'

def loadFILE():
    for file in os.listdir(XML_DIRECTORY):
        if file.find('CRED') == -1 and file.find('XX') == -1 and file.find('GAME') and file.find('txt') != -1:
            print 'file is :' + file
            genXML(XML_DIRECTORY + '/' + file)

def genXML(file):
    utf8Parser = lxml.etree.XMLParser(encoding='utf8')
    doc = lxml.etree.parse(file, utf8Parser)
    root = doc.getroot()
    card = Card()
    cardI18nName = CardI18NName()
    cardI18nFlavorText = CardI18NFlavorText()
    cardI18nTextinhand = CardI18NTextinhand()
    cardI18nHowtogold = CardI18NHowtogold()
    print 'id:' + root.get('CardID')
    card.cardid = root.get('CardID')
    cardI18nName.cardId = root.get('CardID')
    cardI18nFlavorText.cardId = root.get('CardID')
    cardI18nTextinhand.cardId = root.get('CardID')
    cardI18nHowtogold.cardId = root.get('CardID')

    if root.tag == 'Entity':
        tags = doc.getroot().xpath('Tag')
        for elem in tags:
            if elem.get('name') == 'CardName':
                children = elem.getchildren()
                for ch in children:
                    if ch.tag == 'zhCN':
                        card.name = ch.text
                    elif ch.tag == 'enUS':
                        cardI18nName.enUS = ch.text
                    elif ch.tag == 'zhTW':
                        cardI18nName.zhTW = ch.text
            elif elem.get('name') == 'CardSet':
                card.set = elem.get('value')
            elif elem.get('name') == 'CardType':
                card.type = elem.get('value')
            elif elem.get('name') == 'Faction':
                card.faction = elem.get('value')
            elif elem.get('name') == 'Class':
                card.cclass = elem.get('value')
            elif elem.get('name') == 'Rarity':
                card.rarity = elem.get('value')
            elif elem.get('name') == 'Cost':
                card.cost = elem.get('value')
            elif elem.get('name') == 'Atk':
                card.atk = elem.get('value')
            elif elem.get('name') == 'Health':
                card.health = elem.get('value')
            elif elem.get('name') == 'CardTextInHand':
                children = elem.getchildren()
                for ch in children:
                    if ch.tag == 'zhCN':
                        card.textinhand = ch.text
                    elif ch.tag == 'enUS':
                        cardI18nTextinhand.enUS = ch.text
                    elif ch.tag == 'zhTW':
                        cardI18nTextinhand.zhTW = ch.text
            elif elem.get('name') == 'Elite':
                card.elite = elem.get('value')
            elif elem.get('name') == 'Collectible':
                card.collectible = elem.get('value')
            elif elem.get('name') == 'ArtistName':
                card.artist = elem.getchildren()[0].text
            elif elem.get('name') == 'HowToGetThisGoldCard':
                children = elem.getchildren()
                for ch in children:
                    if ch.tag == 'zhCN':
                        card.howtogold = ch.text
                    elif ch.tag == 'enUS':
                        cardI18nHowtogold.enUS = ch.text
                    elif ch.tag == 'zhTW':
                        cardI18nHowtogold.zhTW = ch.text
            elif elem.get('name') == 'FlavorText':
                children = elem.getchildren()
                for ch in children:
                    if ch.tag == 'zhCN':
                        card.flavortext = ch.text
                    elif ch.tag == 'enUS':
                        cardI18nFlavorText.enUS = ch.text
                    elif ch.tag == 'zhTW':
                        cardI18nFlavorText.zhTW = ch.text
            elif elem.get('name') == 'Divine Shield':
                card.divineShield = elem.get('value')
            elif elem.get('name') == 'Taunt':
                card.taunt = elem.get('value')
            elif elem.get('name') == 'Deathrattle':
                card.deathrattle = elem.get('value')
            elif elem.get('name') == 'Race':
                card.race = elem.get('value')
            elif elem.get('name') == 'Battlecry':
                card.battlecry = elem.get('value')
            elif elem.get('name') == 'Combo':
                card.combo = elem.get('value')
            elif elem.get('name') == 'Charge':
                card.charge = elem.get('value')
            elif elem.get('name') == 'Auro':
                card.auro = elem.get('value')
    save(card)
    save(cardI18nFlavorText)
    save(cardI18nHowtogold)
    save(cardI18nName)
    save(cardI18nTextinhand)
    print root.get('CardID') + 'saved!'

def saveCommon():
    print 'start save commo...'
    #saveCardSet()
    #saveCardClass()
    #saveCardType()
    #saveCardRarity()
    saveCardRace()
    saveCardFaction()

def saveCardFaction():
    print 'start save card faction'
    ids = [1,2,3]
    names = [u'部落', u'联盟', u'中立']
    enUSS = [u'Horde', u'Alliance', u'Neutral']
    zhTWS = [u'部落', u'联盟', u'中立']
    for i in range(0,3):
        cf = CardFaction()
        cf.factionId = ids[i]
        cf.name = names[i]
        cf.enUS = enUSS[i]
        cf.zhTW = zhTWS[i]
        save(cf)

def saveCardRace():
    print 'start save card race'
    ids = [1,15,2,24,3,18,4,5,6,17,14,22,7,19,8,20,23,16,9,21,10,11,12]
    names = [u'血精灵', u'恶魔', u'德莱尼', u'龙', u'矮人', u'元素', u'侏儒', u'地精', u'人类', u'机械', u'鱼人', u'蛛魔', u'暗夜精灵', u'食人魔', u'兽人', u'野兽', u'海盗', u'天灾军团', u'牛头人', u'图腾', u'巨魔', u'亡灵', u'狼人']
    enUSS = [u'Blood Elf', u'Demon', u'Draenei', u'Dragon', u'Dwarf', u'Elemental', u'Gnome', u'Goblin', u'Human', u'Mechanical', u'Murloc', u'Nerubian', u'Night Elf', u'Ogre', u'Orc', u'Beast', u'Pirate', u'Scourge', u'Tauren', u'Totem', u'Troll', u'Undead', u'Worgen']
    zhTWS = [u'血精靈', u'惡魔', u'德萊尼', u'龍族', u'矮人', u'元素', u'地精', u'哥布林', u'人類', u'機械', u'魚人', u'奈幽蟲族', u'夜精靈', u'巨魔', u'獸人', u'野獸', u'海盜', u'天譴軍團', u'牛頭人', u'圖騰', u'食人妖', u'不死族', u'狼人']
    for i in range(0,23):
        cr = CardRace()
        cr.raceId = ids[i]
        cr.name = names[i]
        cr.enUS = enUSS[i]
        cr.zhTW = zhTWS[i]
        save(cr)

def saveCardRarity():
    print 'start save card rarity'
    ids = [1,4,2,5,3]
    names = [u'普通', u'史诗', u'免费', u'传说', u'稀有']
    enUSS = [u'Common', u'Epic', u'Free', u'Legendary', u'Rare']
    zhTWS = [u'普通', u'史詩', u'免費', u'傳說', u'精良']
    for i in range(0,5):
        cr = CardRarity()
        cr.rarityId = ids[i]
        cr.name = names[i]
        cr.enUS = enUSS[i]
        cr.zhTW = zhTWS[i]
        save(cr)

def saveCardType():
    print 'start save card type'
    ids = [6,3,10,8,4,5,9,7]
    names = [u'强化', u'英雄', u'英雄技能', u'物品', u'随从', u'法术', u'替代物', u'武器']
    enUSS = [u'Enchantment', u'Hero', u'HeroPower', u'Item', u'Minion', u'Spell', u'Token', u'Weapon']
    zhTWS = [u'附魔', u'英雄', u'英雄能力', u'物品', u'手下', u'法術', u'印記', u'武器']
    for i in range(0,8):
        ct = CardType()
        ct.typeId = ids[i]
        ct.name = names[i]
        ct.enUS = enUSS[i]
        ct.zhTW = zhTWS[i]
        save(ct)

def saveCardClass():
    print 'start save card class'
    ids = [1,2,3,4,5,6,7,8,9,10]
    names = [u'死亡骑士', u'德鲁伊', u'猎人', u'法师', u'圣骑士', u'牧师', u'潜行者', u'萨满祭司', u'术士', u'战士']
    enUSS = [u'Death Knight', u'Druid', u'Hunter', u'Mage', u'Paladin', u'Priest', u'Rogue', u'Shaman', u'Warlock', u'Warrior']
    zhTWS = [u'死亡騎士', u'德魯伊', u'獵人', u'法師', u'聖騎士', u'牧師', u'盜賊', u'薩滿', u'術士', u'戰士']
    for i in range(0,10):
        cs = CardClass()
        cs.classId = ids[i]
        cs.name = names[i]
        cs.enUS = enUSS[i]
        cs.zhTW = zhTWS[i]
        save(cs)

def saveCardSet():
    print 'start save card set...'
    ids = [2,3,4,11]
    names = [u'基本级', u'专家级', u'奖励', u'纪念']
    enUSS = [u'Basic', u'Expert', u'Reward', u'Promo']
    zhTWS = [u'基本牌', u'專家牌', u'獎勵', u'促銷']
    for i in range(0,4):
        cs = CardSet()
        cs.setId = ids[i]
        cs.name = names[i]
        cs.enUS = enUSS[i]
        cs.zhTW = zhTWS[i]
        save(cs)

def save(card):
	db_session.add(card)
	db_session.commit()


if __name__ == '__main__':
    #genXML('hearthstone-data-1.0.0.3937/xml/TextAsset/NEW1_014.txt')
    #loadFILE()
    #saveCommon()
    saveCardClass()