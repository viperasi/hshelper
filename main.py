# -*- coding: utf-8 -*-
from flask import Flask, session, render_template, request, redirect, url_for
from db import db_session
from models import Card
from sqlalchemy import func
import simplejson

app = Flask(__name__)

PER_PAGE = 10

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/mgr')
@app.route('/mgr/index')
@app.route('/mgr/index/<int:page>')
def index(page=1):
    route = 'index'
    result = getCards(page, None)
    return render_template('index.html', cards=result['cards'], allPage=result['allPage'], page=result['page'], route=route)

@app.route('/mgr/hero')
@app.route('/mgr/hero/<int:page>')
def hero(page=1):
    route = 'hero'
    result = getCards(page, u'英雄')
    return render_template('index.html', cards=result['cards'], allPage=result['allPage'], page=result['page'], route=route)

@app.route('/mgr/hskill')
@app.route('/mgr/hskill/<int:page>')
def heroskill(page=1):
    route = 'hskill'
    result = getCards(page, u'英雄技能')
    return render_template('index.html', cards=result['cards'], allPage=result['allPage'], page=result['page'], route=route)

@app.route('/mgr/weapon')
@app.route('/mgr/weapon/<int:page>')
def weapon(page=1):
    route = 'weapon'
    result = getCards(page, u'武器')
    return render_template('index.html', cards=result['cards'], allPage=result['allPage'], page=result['page'],  route=route)

@app.route('/mgr/skill')
@app.route('/mgr/skill/<int:page>')
def skill(page=1):
    route = 'skill'
    result = getCards(page, u'技能')
    return render_template('index.html', cards=result['cards'], allPage=result['allPage'], page=result['page'],  route=route)

@app.route('/mgr/ally')
@app.route('/mgr/ally/<int:page>')
def ally(page=1):
    route = 'ally'
    result = getCards(page, u'随从')
    return render_template('index.html', cards=result['cards'], allPage=result['allPage'], page=result['page'],  route=route)

@app.route('/card/<int:id>')
def card(id=None):
    if id is not None:
        card = Card.query.filter(Card.id == id).first()

        return simplejson.dumps(card.__json__())

def getCards(page=1, type=None):
    result = {
        'cards' : None,
        'allPage' : 0,
        'page' : page
    }
    count = 0
    if type is None:
        count = db_session.query(func.count(Card.id)).first()[0]
    else:
        count = db_session.query(func.count(Card.id)).filter(Card.card_type == type).first()[0]
    curr = (page -1)  * PER_PAGE
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