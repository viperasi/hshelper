# -*- coding: utf-8 -*-
import urllib2
#import html5lib
#from html5lib import treebuilders, treewalkers, serializer
from BeautifulSoup import BeautifulSoup
from models import Card
from db import db_session

HOST = 'http://db.h.163.com/cards/filter?filter=CardType'
HERO_FILTER = {
	'param'		:		'%3D3',
	'page'		:		2,
	'count'		:		7
}

SKILL_FILTER = {
	'param'		:		'%3D5',
	'page'		:		19,
	'count'		:		7
}

HERO_SKILL_FILTER = {
	'param'		:		'%3D10',
	'page'		:		2,
	'count'		:		4
}

WEAPON_FILTER = {
	'param'		:		'%3D7',
	'page'		:		2,
	'count'		:		9
}

ALLY_FILTER = {
	'param'		:		'%3D4',
	'page'		:		28,
	'count'		:		10
}


def getContent(url):
	print url
	response = urllib2.urlopen(url)
	return response.read()

def genData(html, type):
	soup = BeautifulSoup(html)
	divs = soup.findAll('div', 'card clearfix')
	if type == 'HERO':
		return genHERO(divs)
	elif type == 'HEROSKILL':
		return genHEROSKILL(divs)
	elif type == 'WEAPON':
		return genWEAPON(divs)
	elif type == 'SKILL':
		return genSKILL(divs)
	elif type == 'ALLY':
		return genALLY(divs)
	return None

def genHERO(divs):
	cards = []
	card_type = u'英雄'
	for div in divs:
		a = div.find('div', 'card-image').find('a')
		img = a.find('img')
		card_img = img['src']
		attrdiv = div.find('div', 'card-attribute')
		card_name = attrdiv.find('h2').find('a').text
		lis = attrdiv.find('ul').findAll('li')
		card_class = None
		card_race = None
		card_rarity = None
		card_set = None
		card_collectible = None
		for li in lis:
			a = li.find('a')
			if a is not None:
				if a['href'].find('Class') != -1:
					card_class = a.span.text
				elif a['href'].find('Race') != -1:
					card_race = a.text
				elif a['href'].find('Rarity') != -1:
					card_rarity = a.span.text
				elif a['href'].find('CardSet') != -1:
					card_set = a.text
			else:
				card_collectible = li.text
		card = Card(card_name=card_name,
					card_type=card_type,
					card_img=card_img,
					card_class=card_class,
					card_rarity=card_rarity,
					card_set=card_set,
					card_collectible=card_collectible)
		cards.append(card)
	return cards

def genSKILL(divs):
	cards = []
	card_type = u'技能'
	for div in divs:
		a = div.find('div', 'card-image').find('a')
		img = a.find('img')
		card_img = img['src']
		attrdiv = div.find('div', 'card-attribute')
		card_name = attrdiv.find('h2').find('a').text
		card_desc = None
		card_remark = None
		if attrdiv.findAll('p') is not None:
			p = attrdiv.findAll('p')
			for pi in p:
				if pi.has_key('class'):
					card_remark = pi.text
				else:
					card_desc = pi.text

		lis = attrdiv.find('ul').findAll('li')
		card_class = None
		card_race = None
		card_rarity = None
		card_set = None
		for li in lis:
			a = li.find('a')
			if a is not None:
				if a['href'].find('Class') != -1:
					card_class = a.span.text
				elif a['href'].find('Race') != -1:
					card_race = a.text
				elif a['href'].find('Rarity') != -1:
					card_rarity = a.span.text
				elif a['href'].find('CardSet') != -1:
					card_set = a.text
		card = Card(card_name=card_name,
					card_type=card_type,
					card_img=card_img,
					card_class=card_class,
					card_rarity=card_rarity,
					card_set=card_set,
					card_desc=card_desc,
					card_remark=card_remark)
		cards.append(card)
	return cards

def genHEROSKILL(divs):
	cards = []
	card_type = u'英雄技能'
	for div in divs:
		a = div.find('div', 'card-image').find('a')
		img = a.find('img')
		card_img = img['src']
		attrdiv = div.find('div', 'card-attribute')
		card_name = attrdiv.find('h2').find('a').text
		card_desc = attrdiv.p.text
		lis = attrdiv.find('ul').findAll('li')
		card_class = None
		card_race = None
		card_rarity = None
		card_set = None
		card_collectible = None
		for li in lis:
			a = li.find('a')
			if a is not None:
				if a['href'].find('Class') != -1:
					card_class = a.span.text
				elif a['href'].find('Race') != -1:
					card_race = a.text
				elif a['href'].find('Rarity') != -1:
					card_rarity = a.span.text
				elif a['href'].find('CardSet') != -1:
					card_set = a.text
			else:
				card_collectible = li.text
		card = Card(card_name=card_name,
					card_type=card_type,
					card_img=card_img,
					card_class=card_class,
					card_rarity=card_rarity,
					card_set=card_set,
					card_desc=card_desc)
		cards.append(card)
	return cards

def genWEAPON(divs):
	cards = []
	card_type = u'武器'
	for div in divs:
		a = div.find('div', 'card-image').find('a')
		img = a.find('img')
		card_img = img['src']
		attrdiv = div.find('div', 'card-attribute')
		card_name = attrdiv.find('h2').find('a').text
		card_desc = None
		card_remark = None
		if attrdiv.findAll('p') is not None:
			p = attrdiv.findAll('p')
			for pi in p:
				if pi.has_key('class'):
					card_remark = pi.text
				else:
					card_desc = pi.text

		lis = attrdiv.find('ul').findAll('li')
		card_class = None
		card_race = None
		card_rarity = None
		card_set = None
		for li in lis:
			a = li.find('a')
			if a is not None:
				if a['href'].find('Class') != -1:
					card_class = a.span.text
				elif a['href'].find('Race') != -1:
					card_race = a.text
				elif a['href'].find('Rarity') != -1:
					card_rarity = a.span.text
				elif a['href'].find('CardSet') != -1:
					card_set = a.text
		card = Card(card_name=card_name,
					card_type=card_type,
					card_img=card_img,
					card_class=card_class,
					card_rarity=card_rarity,
					card_set=card_set,
					card_desc=card_desc,
					card_remark=card_remark)
		cards.append(card)
	return cards

def genALLY(divs):
	cards = []
	card_type = u'随从'
	for div in divs:
		a = div.find('div', 'card-image').find('a')
		img = a.find('img')
		card_img = img['src']
		attrdiv = div.find('div', 'card-attribute')
		card_name = attrdiv.find('h2').find('a').text
		card_desc = None
		card_remark = None
		if attrdiv.findAll('p') is not None:
			p = attrdiv.findAll('p')
			for pi in p:
				if pi.has_key('class'):
					card_remark = pi.text
				else:
					card_desc = pi.text

		lis = attrdiv.find('ul').findAll('li')
		card_class = None
		card_race = None
		card_rarity = None
		card_set = None
		for li in lis:
			a = li.find('a')
			if a is not None:
				if a['href'].find('Class') != -1:
					card_class = a.span.text
				elif a['href'].find('Race') != -1:
					card_race = a.text
				elif a['href'].find('Rarity') != -1:
					card_rarity = a.span.text
				elif a['href'].find('CardSet') != -1:
					card_set = a.text
		card = Card(card_name=card_name,
					card_type=card_type,
					card_img=card_img,
					card_class=card_class,
					card_rarity=card_rarity,
					card_set=card_set,
					card_desc=card_desc,
					card_remark=card_remark)
		cards.append(card)
	return cards

def save(card):
	db_session.add(card)
	db_session.commit()

def genAll():
	#HERO
	for i in range(1, HERO_FILTER['page'] + 1):
		url = HOST + HERO_FILTER['param'] + '&page=' + str(i)
		html = getContent(url)
		cards = genData(html, 'HERO')
		for card in cards:
			save(card)

	#HEROSKILL
	for i in range(1, HERO_SKILL_FILTER['page'] + 1):
		url = HOST + HERO_SKILL_FILTER['param'] + '&page=' + str(i)
		html = getContent(url)
		cards = genData(html, 'HEROSKILL')
		for card in cards:
			save(card)

	#WEAPON
	for i in range(1, WEAPON_FILTER['page'] + 1):
		url = HOST + WEAPON_FILTER['param'] + '&page=' + str(i)
		html = getContent(url)
		cards = genData(html, 'WEAPON')
		for card in cards:
			save(card)

	#SKILL
	for i in range(1, SKILL_FILTER['page'] + 1):
		url = HOST + SKILL_FILTER['param'] + '&page=' + str(i)
		html = getContent(url)
		cards = genData(html, 'SKILL')
		for card in cards:
			save(card)

	#ALLY
	for i in range(1, ALLY_FILTER['page'] + 1):
		url = HOST + ALLY_FILTER['param'] + '&page=' + str(i)
		html = getContent(url)
		cards = genData(html, 'ALLY')
		for card in cards:
			save(card)


if __name__ == '__main__':
	genAll()