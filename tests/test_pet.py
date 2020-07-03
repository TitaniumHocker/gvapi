# -*- coding: utf-8 -*-
from gvapi import Hero
from gvapi.hero import requests
from gvapi.pet import Pet


def test_pet_attributes(mocked_get_t, monkeypatch):
    monkeypatch.setattr(requests, 'get', mocked_get_t)
    hero = Hero('Mars', token='awdpiawjdpajdwpoajdap')
    assert isinstance(hero.pet, Pet)
    assert hero.pet.name == 'Бублик «Обжора»'
    assert hero.pet.class_name == 'хохмяк'
    assert hero.pet.level == 5
    assert not hero.pet.wounded
    assert hero.pet.__repr__() == '<Pet {}, class: {}>'.format(hero.pet.name, hero.pet.class_name)
    assert hero.pet.__str__() == 'Питомец {} "{}"'.format(hero.pet.class_name, hero.pet.name)
