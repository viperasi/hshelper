# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, Text, DateTime
from db import Base
from datetime import datetime

class Card(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True)
    cardid = Column(Text)
    name = Column(Text)
    set = Column(Text)
    type = Column(Text)
    faction = Column(Text)
    cclass = Column(Text)
    rarity = Column(Text)
    cost = Column(Integer)
    atk = Column(Integer)
    health = Column(Integer)
    textinhand = Column(Text)
    collectible = Column(Integer)
    artist = Column(Text)
    howtogold = Column(Text)
    flavortext = Column(Text)
    taunt = Column(Integer)
    elite = Column(Integer)
    race = Column(Text)
    combo = Column(Integer)
    charge = Column(Integer)
    enrage = Column(Integer)
    auro = Column(Integer)
    divineShield = Column(Integer)
    deathrattle = Column(Integer)
    battlecry = Column(Integer)
    img = Column(Text)


    def __init__(self, name=None,
                        cardid=None,
                        set=None,
                        type=None,
                        faction=None,
                        cclass=None,
                        rarity=None,
                        cost=None,
                        atk=None,
                        health=None,
                        textinhand=None,
                        collectible=None,
                        artist=None,
                        howtogold=None,
                        flavortext=None,
                        taunt=None,
                        elite=None,
                        race=None,
                        combo=None,
                        charge=None,
                        enrage=None,
                        auro=None):
        self.name = name
        self.cardid = cardid
        self.set = set
        self.type = type
        self.faction = faction
        self.cclass = cclass
        self.rarity = rarity
        self.cost = cost
        self.atk = atk
        self.health = health
        self.textinhand = textinhand
        self.collectible = collectible
        self.artist = artist
        self.howtogold = howtogold
        self.flavortext = flavortext
        self.taunt = taunt
        self.elite = elite
        self.race = race
        self.combo = combo
        self.charge = charge
        self.enrage = enrage
        self.auro = auro

class CardI18NName(Base):
    __tablename__ = 'cards_i18n_name'
    id = Column(Integer, primary_key=True)
    cardId = Column(Integer)
    enUS = Column(Text)
    zhTW = Column(Text)

    def __init__(self, cardId=None,
                        enUS=None,
                        zhTW=None):
        self.cardId = cardId
        self.enUS = enUS
        self.zhTW = zhTW

class CardI18NTextinhand(Base):
    __tablename__ = 'cards_i18n_textinhand'
    id = Column(Integer, primary_key=True)
    cardId = Column(Integer)
    enUS = Column(Text)
    zhTW = Column(Text)

    def __init__(self, cardId=None,
                        enUS=None,
                        zhTW=None):
        self.cardId = cardId
        self.enUS = enUS
        self.zhTW = zhTW

class CardI18NFlavorText(Base):
    __tablename__ = 'cards_i18n_flavortext'
    id = Column(Integer, primary_key=True)
    cardId = Column(Integer)
    enUS = Column(Text)
    zhTW = Column(Text)

    def __init__(self, cardId=None,
                        enUS=None,
                        zhTW=None):
        self.cardId = cardId
        self.enUS = enUS
        self.zhTW = zhTW

class CardI18NHowtogold(Base):
    __tablename__ = 'cards_i18n_howtogold'
    id = Column(Integer, primary_key=True)
    cardId = Column(Integer)
    enUS = Column(Text)
    zhTW = Column(Text)

    def __init__(self, cardId=None,
                        enUS=None,
                        zhTW=None):
        self.cardId = cardId
        self.enUS = enUS
        self.zhTW = zhTW

class CardSet(Base):
    __tablename__ = 'card_set'
    id = Column(Integer, primary_key=True)
    setId = Column(Integer)
    name = Column(Text)
    enUS = Column(Text)
    zhTW = Column(Text)

    def __init__(self,setId=None,
                        name=None,
                        enUS=None,
                        zhTW=None):
        self.setId = setId
        self.name = name
        self.enUS = enUS
        self.zhTW = zhTW

class CardType(Base):
    __tablename__ = 'card_type'
    id = Column(Integer, primary_key=True)
    typeId = Column(Integer)
    name = Column(Text)
    enUS = Column(Text)
    zhTW = Column(Text)

    def __init__(self, typeId=None,
                        name=None,
                        enUS=None,
                        zhTW=None):
        self.typeId = typeId
        self.name = name
        self.enUS = enUS
        self.zhTW = zhTW

class CardClass(Base):
    __tablename__ = 'card_class'
    id = Column(Integer, primary_key=True)
    classId = Column(Integer)
    name = Column(Text)
    enUS = Column(Text)
    zhTW = Column(Text)

    def __init__(self, classId=None,
                        name=None,
                        enUS=None,
                        zhTW=None):
        self.classId = classId
        self.name = name
        self.enUS = enUS
        self.zhTW = zhTW

class CardFaction(Base):
    __tablename__ = 'card_faction'
    id = Column(Integer, primary_key=True)
    factionId = Column(Integer)
    name = Column(Text)
    enUS = Column(Text)
    zhTW = Column(Text)

    def __init__(self, factionId=None,
                        name=None,
                        enUS=None,
                        zhTW=None):
        self.factionId = factionId
        self.name = name
        self.enUS = enUS
        self.zhTW = zhTW

class CardRace(Base):
    __tablename__ = 'card_race'
    id = Column(Integer, primary_key=True)
    raceId = Column(Integer)
    name = Column(Text)
    enUS = Column(Text)
    zhTW = Column(Text)

    def __init__(self, raceId=None,
                        name=None,
                        enUS=None,
                        zhTW=None):
        self.raceId = raceId
        self.name = name
        self.enUS = enUS
        self.zhTW = zhTW

class CardRarity(Base):
    __tablename__ = 'card_rarity'
    id = Column(Integer, primary_key=True)
    rarityId = Column(Integer)
    name = Column(Text)
    enUS = Column(Text)
    zhTW = Column(Text)

    def __init__(self, rarityId=None,
                        name=None,
                        enUS=None,
                        zhTW=None):
        self.rarityId = rarityId
        self.name = name
        self.enUS = enUS
        self.zhTW = zhTW

class Share(Base):
    __tablename__ = 'shares'
    id = Column(Integer, primary_key=True)
    share_shorturl = Column(Text)
    share_qiniuurl = Column(Text)
    share_createtime = Column(DateTime)
    share_enabled = Column(Integer)
    share_deleted = Column(Text)

    def __init__(self, share_shorturl=None, share_qiniuurl=None):
        self.share_shorturl = share_shorturl
        self.share_qiniuurl = share_qiniuurl
        self.share_deleted = 0
        self.share_enabled = 1
        self.share_createtime = datetime.now()