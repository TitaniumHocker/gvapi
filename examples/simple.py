#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gvapi import Hero

hero = Hero('Mars', token='awudhawiudh')

print('Золото: {}, Кирпичи: {}'.format(hero.gold, hero.bricks))
