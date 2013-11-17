# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, Text, DateTime
from db import Base
from datetime import datetime

class Card(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True)
    card_name = Column(Text)
    card_engname = Column(Text)
    card_type = Column(Text)
    card_class = Column(Text)
    card_rarity = Column(Text)
    card_set = Column(Text)
    card_race = Column(Text)
    card_faction = Column(Text)
    card_crafting = Column(Text)
    card_gained = Column(Text)
    card_artist = Column(Text)
    card_collectible = Column(Text)
    card_elite = Column(Text)
    card_cost = Column(Text)
    card_att = Column(Text)
    card_hp = Column(Text)
    card_img = Column(Text)
    card_engimg = Column(Text)
    card_desc = Column(Text)
    card_engdesc = Column(Text)
    card_remark = Column(Text)
    card_engremark = Column(Text)
    card_maxnum = Column(Integer)
    card_num = Column(Integer)

    def __init__(self, card_name=None,card_type=None,card_class=None,card_rarity=None,card_set=None,card_race=None,card_faction=None,card_crafting=None,card_gained=None,card_artist=None,card_collectible=None,card_elite=None,card_cost=None,card_att=None,card_hp=None,card_img=None,card_desc=None,card_remark=None):
        self.card_name = card_name
        self.card_type = card_type
        self.card_class = card_class
        self.card_rarity = card_rarity
        self.card_set = card_set
        self.card_race = card_race
        self.card_faction = card_faction
        self.card_crafting = card_crafting
        self.card_gained = card_gained
        self.card_artist = card_artist
        self.card_collectible = card_collectible
        self.card_elite = card_elite
        self.card_cost = card_cost
        self.card_att = card_att
        self.card_hp = card_hp
        self.card_img = card_img
        self.card_desc = card_desc
        self.card_remark = card_remark

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