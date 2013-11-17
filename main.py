# -*- coding: utf-8 -*-
from flask import Flask, session, render_template, request, redirect, url_for, abort
from db import db_session
from models import Card
from picutil import saveImage
from sqlalchemy import func
import simplejson


app = Flask(__name__)

PER_PAGE = 10

QINIU_HOST = 'http://hshelper.u.qiniudn.com/'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


#mgr start
@app.route('/mgr')
@app.route('/mgr/index')
@app.route('/mgr/index/<int:page>')
def mgrIndex(page=1):
    route = 'index'
    result = getCards(page, None)
    return render_template('mgr/index.html', cards=result['cards'], allPage=result['allPage'], page=result['page'], route=route)

@app.route('/mgr/hero')
@app.route('/mgr/hero/<int:page>')
def mgrHero(page=1):
    route = 'hero'
    result = getCards(page, u'英雄')
    return render_template('mgr/index.html', cards=result['cards'], allPage=result['allPage'], page=result['page'], route=route)

@app.route('/mgr/hskill')
@app.route('/mgr/hskill/<int:page>')
def mgrHeroSkill(page=1):
    route = 'hskill'
    result = getCards(page, u'英雄技能')
    return render_template('mgr/index.html', cards=result['cards'], allPage=result['allPage'], page=result['page'], route=route)

@app.route('/mgr/weapon')
@app.route('/mgr/weapon/<int:page>')
def mgrWeapon(page=1):
    route = 'weapon'
    result = getCards(page, u'武器')
    return render_template('mgr/index.html', cards=result['cards'], allPage=result['allPage'], page=result['page'],  route=route)

@app.route('/mgr/skill')
@app.route('/mgr/skill/<int:page>')
def mgrSkill(page=1):
    route = 'skill'
    result = getCards(page, u'技能')
    return render_template('mgr/index.html', cards=result['cards'], allPage=result['allPage'], page=result['page'],  route=route)

@app.route('/mgr/ally')
@app.route('/mgr/ally/<int:page>')
def mgrAlly(page=1):
    route = 'ally'
    result = getCards(page, u'随从')
    return render_template('mgr/index.html', cards=result['cards'], allPage=result['allPage'], page=result['page'],  route=route)

@app.route('/mgr/edit/<int:id>')
def mgrEdit(id=None):
    if id is not None:
        card = Card.query.filter(Card.id == id).first()
        if card is not None:
            return render_template('mgr/edit.html', card=card)
    abort(404)

@app.route('/mgr/save/<int:id>', methods=['POST'])
def mgrSave(id=None):
    if id is not None:
        card = Card.query.filter(Card.id == id).first()
        if card is not None:
            if request.form['name'] is not None and request.form['name'] != 'None':
                card.card_name = request.form['name']
            if request.form['engname'] is not None and request.form['engname'] != 'None':
                card.card_engname = request.form['engname']
            if request.form['type'] is not None and request.form['type'] != 'None':
                card.card_type = request.form['type']
            if request.form['rarity'] is not None and request.form['rarity'] != 'None':
                card.card_rarity = request.form['rarity']
            if request.form['class'] is not None and request.form['class'] != 'None':
                card.card_class = request.form['class']
            if request.form['set'] is not None and request.form['set'] != 'None':
                card.card_set = request.form['set']
            if request.form['race'] is not None and request.form['race'] != 'None':
                card.card_race = request.form['race']
            if request.form['faction'] is not None and request.form['faction'] != 'None':
                card.card_faction = request.form['faction']
            if request.form['collectible'] is not None and request.form['collectible'] != 'None':
                card.card_collectible = request.form['collectible']
            if request.form['crafting'] is not None and request.form['crafting'] != 'None':
                card.card_crafting = request.form['crafting']
            if request.form['gained'] is not None and request.form['gained'] != 'None':
                card.card_gained = request.form['gained']
            if request.form['artist'] is not None and request.form['artist'] != 'None':
                card.card_artist = request.form['artist']
            if request.form['cost'] is not None and request.form['cost'] != 'None':
                card.card_cost = request.form['cost']
            if request.form['att'] is not None and request.form['att'] != 'None':
                card.card_att = request.form['att']
            if request.form['hp'] is not None and request.form['hp'] != 'None':
                card.card_hp = request.form['hp']
            if request.form['img'] is not None and request.form['img'] != 'None':
                card.card_img = request.form['img']
            if request.form['engimg'] is not None and request.form['engimg'] != 'None':
                card.card_engimg = request.form['engimg']
            if request.form['desc'] is not None and request.form['desc'] != 'None':
                card.card_desc = request.form['desc']
            if request.form['engdesc'] is not None and request.form['engdesc'] != 'None':
                card.card_engdesc = request.form['engdesc']
            if request.form['remark'] is not None and request.form['remark'] != 'None':
                card.card_remark = request.form['remark']
            if request.form['engremark'] is not None and request.form['engremark'] != 'None':
                card.card_engremark = request.form['engremark']
            db_session.merge(card)
            db_session.commit()
            return redirect(url_for('mgrIndex'))
    abort(404)
#mgr end

#index start
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set/<string:cardstr>')
def set(cardstr=None):
    herostr = None
    cardsstr = None
    if cardstr is not None:
        strArr = cardstr.split('&')
        herostr = strArr[0]
        print(herostr)
        if len(strArr) > 1:
            cardsstr = strArr[1]
        classcards = None
        allycards = None
        cards = None
        cs = ''
        if herostr is not None:
            classcards = Card.query.filter(Card.card_class == herostr, Card.card_type != u'英雄', Card.card_type != u'英雄技能')
            allycards = Card.query.filter(Card.card_type == u'随从')
        if cardsstr is not None:
            cardsNumArr = cardsstr.split(';')
            cardIds = []
            for cardNumStr in cardsNumArr:
                if cardNumStr is not None and cardNumStr != '':
                    cardIds.append(cardNumStr.split(':')[0])
            cards = Card.query.filter(Card.id.in_(cardIds)).all()
            for c in cards:
                for cardNumStr in cardsNumArr:
                    cns = cardNumStr.split(':')
                    if cns[0] is not None and cns[0] != '' and c.id == int(cns[0]):
                        cs = cs + str(c.id) + ':' + c.card_name + ':' + cns[1] + ';'
                    else:
                        continue
        return render_template('set.html', classcards=classcards, allycards=allycards, herostr=herostr, cards=cards, cs=cs)
    return redirect(url_for('index'))

@app.route('/share/<string:cls>', methods=['POST'])
def share(cls=None):
    return QINIU_HOST + 'FpjWFB07cmjwUBiPNUibjvMiwZIH'
    if cls is not None:
        hero = Card.query.filter(Card.card_class == cls, Card.card_type == u'英雄', Card.card_rarity == u'免费', Card.card_set == u'基础').first()
        if request.form['cardsstr'] is not None:
            cardsstr = request.form['cardsstr']
            cardsNumArr = cardsstr.split(';')
            cardIds = []
            for cardNumStr in cardsNumArr:
                if cardNumStr is not None and cardNumStr != '':
                    cardIds.append(cardNumStr.split(':')[0])
            cards = Card.query.filter(Card.id.in_(cardIds)).all()
            for c in cards:
                for cardNumStr in cardsNumArr:
                    cns = cardNumStr.split(':')
                    if cns[0] is not None and cns[0] != '' and c.id == int(cns[0]):
                        c.card_num = cns[1]
                    else:
                        continue
            share = saveImage(hero, cards)
            return QINIU_HOST + share.share_qiniuurl
    abort(404)

@app.route('/db')
@app.route('/db/index')
@app.route('/db/<int:page>')
@app.route('/db/index/<int:page>')
def db(page=1):
    route = 'index'
    result = getCards(page, None)
    return render_template('db.html', cards=result['cards'], allPage=result['allPage'], page=result['page'], route=route)

@app.route('/db/hero')
@app.route('/db/hero/<int:page>')
def dbHero(page=1):
    route = 'hero'
    result = getCards(page, u'英雄')
    return render_template('db.html', cards=result['cards'], allPage=result['allPage'], page=result['page'], route=route)

@app.route('/db/hskill')
@app.route('/db/hskill/<int:page>')
def dbHeroSkill(page=1):
    route = 'hskill'
    result = getCards(page, u'英雄技能')
    return render_template('db.html', cards=result['cards'], allPage=result['allPage'], page=result['page'], route=route)

@app.route('/db/weapon')
@app.route('/db/weapon/<int:page>')
def dbWeapon(page=1):
    route = 'weapon'
    result = getCards(page, u'武器')
    return render_template('db.html', cards=result['cards'], allPage=result['allPage'], page=result['page'], route=route)

@app.route('/db/skill')
@app.route('/db/skill/<int:page>')
def dbSkill(page=1):
    route = 'skill'
    result = getCards(page, u'技能')
    return render_template('db.html', cards=result['cards'], allPage=result['allPage'], page=result['page'], route=route)

@app.route('/db/ally')
@app.route('/db/ally/<int:page>')
def dbAlly(page=1):
    route = 'ally'
    result = getCards(page, u'随从')
    return render_template('db.html', cards=result['cards'], allPage=result['allPage'], page=result['page'], route=route)
#index end

@app.route('/card/<int:id>')
def card(id=None):
    if id is not None:
        card = Card.query.filter(Card.id == id).first()
        return simplejson.dumps(card.__json__())
    abort(404)

def getCards(page=1, type=None):
    result = {
        'cards': None,
        'allPage': 0,
        'page': page
    }
    count = 0
    if type is None:
        count = db_session.query(func.count(Card.id)).first()[0]
    else:
        count = db_session.query(func.count(Card.id)).filter(Card.card_type == type).first()[0]
    curr = (page - 1) * PER_PAGE
    allPage = 1
    if count % PER_PAGE == 0 :
        allPage = count / PER_PAGE
    else:
        allPage = int(count / PER_PAGE) + 1
    if curr > count:
        curr = count
        page = allPage
    if curr < 0:
        curr = 1
        page = 1
    cards = None
    if type is None:
        cards = Card.query.order_by(Card.id)[curr : curr + PER_PAGE]
    else:
        cards = Card.query.filter(Card.card_type == type).order_by(Card.id)[curr : curr + PER_PAGE]
    result['cards'] = cards
    result['allPage'] = allPage
    result['page'] = page
    return result

if __name__ == '__main__':
    app.secret_key = 'why would I tell you my secret key?'
    app.debug = True
    app.run()