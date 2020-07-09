# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import pytest

from gvapi import Hero
from gvapi import errors
from gvapi.hero import requests


def test_create_without_token(mocked_get, monkeypatch):
    monkeypatch.setattr(requests, 'get', mocked_get)
    hero = Hero('Mars')
    assert isinstance(hero, Hero)
    assert hero.god == 'Mars'
    assert hero.name == 'Gaius Iulius Caesar'


def test_create_with_token(mocked_get_t, monkeypatch):
    monkeypatch.setattr(requests, 'get', mocked_get_t)
    hero = Hero('Mars', token='aoidhaodwjaodwhaoidw')
    assert isinstance(hero, Hero)
    assert hero.is_alive


@pytest.mark.parametrize('name', ('is_alive', 'health', 'health_percent', 'gold', 'activatables',
                                  'is_fighting', 'fight_type', 'aura', 'diary_last', 'distance',
                                  'exp', 'expired', 'godpower', 'godpower_percent', 'inventory_num',
                                  'inventory', 'quest_progress', 'quest', 'town_name'))
def test_tokenized_exceptions(name, mocked_get, monkeypatch):
    monkeypatch.setattr(requests, 'get', mocked_get)
    hero = Hero('Mars')
    with pytest.raises(errors.NeedToken):
        hero.__getattribute__(name)



def test_basic(mocked_get_t, monkeypatch):
    monkeypatch.setattr(requests, 'get', mocked_get_t)
    hero = Hero('Mars', token='aoiwdjawodijadw1234')
    assert hero.data == mocked_get_t().json()
    assert hero.__repr__() == '<Hero {}>'.format(hero.name)
    assert hero.__str__() == 'Герой {}'.format(hero.name)
    assert hero.__getattribute__('_Hero__get_data')() == mocked_get_t().json()
    assert hero.token.startswith('****') and hero.token.endswith('1234')

    assert hero.threshold == 300
    hero.threshold = 200
    assert hero.threshold == 200

    hero.data['gender'] = 'female'
    assert hero.__str__() == 'Героиня {}'.format(hero.name)


def test_nontokenized_attributes(mocked_get, monkeypatch):
    monkeypatch.setattr(requests, 'get', mocked_get)
    data = mocked_get().json()
    hero = Hero('Mars')

    assert hero.name == data['name']
    assert hero.god == data['godname']
    assert hero.gender == 'муж'
    assert hero.level == data['level']
    assert hero.max_health == data['max_health']
    assert hero.motto == data['motto']
    assert hero.clan == data['clan']
    assert hero.clan_pos == data['clan_position']
    assert hero.max_godpower == 100
    assert hero.inventory_max_num == data['inventory_max_num']
    assert hero.words == 0
    assert hero.ark == (100, 100)
    assert hero.arena == (data['arena_won'], data['arena_lost'])
    assert hero.alignment == data['alignment']
    assert hero.bricks == data['bricks_cnt']
    assert hero.bricks_percent == data['bricks_cnt'] / 1000 * 100


def test_tokenized_attributes(mocked_get_t, monkeypatch):
    monkeypatch.setattr(requests, 'get', mocked_get_t)
    data = mocked_get_t().json()
    hero = Hero('Mars', token='aoiwdjaoiwjd')
    assert hero.is_alive
    assert hero.health == data['health']
    assert hero.health_percent == data['health'] / data['max_health']
    assert hero.gold == data['gold_approx']
    assert hero.activatables == data['activatables']
    assert hero.is_fighting == data['arena_fight']
    assert hero.fight_type == ''
    assert hero.aura == ''
    assert hero.diary_last == data['diary_last']
    assert hero.distance == data['distance']
    assert hero.exp == data['exp_progress']
    assert not hero.expired
    assert hero.godpower == data['godpower']
    assert hero.godpower_percent == data['godpower'] / 100
    assert hero.inventory_num == data['inventory_num']
    assert hero.inventory == (data['inventory_num'],
                              data['inventory_max_num'],
                              data['activatables'])
    assert hero.quest_progress == data['quest_progress']
    assert hero.quest == data['quest']
    assert hero.town_name == data['town_name']
