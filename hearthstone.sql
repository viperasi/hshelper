/*
drop table if exists card_type;
create table card_type(
	id integer primary key autoincrement,
	name text not null
);

drop table if exists card_class;
create table card_class(
	id integer primary key autoincrement,
	name text not null
);

drop table if exists card_rarity;
create table card_rarity(
	id integer primary key autoincrement,
	name text not null
);

drop table if exists card_set;
create table card_set(
	id integer primary key autoincrement,
	name text not null
);

drop table if exists card_race;
create table card_race(
	id integer primary key autoincrement,
	name text not null
);

drop table if exists card_fuction;
create table card_fuction(
	id integer primary key autoincrement,
	name text not null
);
*/
drop table if exists cards;
create table cards(
	id integer primary key autoincrement,
	card_name text not null,
	card_engname text not null,
	card_type text,
	card_class text,
	card_rarity text,
	card_set text,
	card_race text,
	card_faction text,
	card_crafting integer,
	card_gained integer,
	card_artist text,
	card_collectible text,
	card_elite text,
	card_cost integer,
	card_att integer,
	card_hp integer,
	card_desc text,
	card_engdesc text,
	card_remark text,
	card_engremark text
);