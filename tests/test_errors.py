# -*- coding: utf-8 -*-
import pytest

from gvapi import Hero
from gvapi import errors
from gvapi.hero import requests
from gvapi.hero import json


def raise_(ex):
    raise ex()


class UnexpectedResponseCode:
    status_code = 666
    text = 'some shit'


class UnexpectedResponseJson:
    status_code = 200
    text = 'some shit'

    @staticmethod
    def json():
        raise json.decoder.JSONDecodeError('a', 'b', 3)


def test_unavailable(monkeypatch):
    monkeypatch.setattr(requests, 'get', lambda *args, **kwargs: raise_(requests.ConnectTimeout))
    with pytest.raises(errors.APIUnavailable):
        hero = Hero('someone')
        hero.sync()


def test_unexpected_code(monkeypatch):
    monkeypatch.setattr(requests, 'get', lambda *args, **kwargs: UnexpectedResponseCode())
    with pytest.raises(errors.UnexpectedAPIResponse):
        hero = Hero('someone')
        hero.sync()


def test_unexpected_json(monkeypatch):
    monkeypatch.setattr(requests, 'get', lambda *args, **kwargs: UnexpectedResponseJson())
    with pytest.raises(errors.UnexpectedAPIResponse):
        hero = Hero('someone')
        hero.sync()


def test_resetted(mocked_get_t, monkeypatch):
    monkeypatch.setattr(requests, 'get', mocked_get_t)
    hero = Hero('Mars', token='awuidhawudihaiwudh')
    health = hero.data.pop('health')
    with pytest.raises(errors.InvalidToken):
        hero.is_alive
    hero.data['health'] = health


def test_need_token(mocked_get, monkeypatch):
    monkeypatch.setattr(requests, 'get', mocked_get)
    hero = Hero('Mars')
    with pytest.raises(errors.NeedToken):
        hero.health


def test_min_threshold(mocked_get, monkeypatch):
    monkeypatch.setattr(requests, 'get', mocked_get)
    with pytest.raises(errors.MinThresholdException):
        hero = Hero('Mars', threshold=1)
    hero = Hero('Mars')
    with pytest.raises(errors.MinThresholdException):
        hero.threshold = 1


def test_temple(mocked_get, monkeypatch):
    monkeypatch.setattr(requests, 'get', mocked_get)
    hero = Hero('Mars')
    with pytest.raises(errors.TheTempleIsUndone):
        hero.temple_completed_at


def test_ark(mocked_get, monkeypatch):
    monkeypatch.setattr(requests, 'get', mocked_get)
    hero = Hero('Mars')
    with pytest.raises(errors.TheArkIsUndone):
        hero.ark_completed_at


def test_savings(mocked_get, monkeypatch):
    monkeypatch.setattr(requests, 'get', mocked_get)
    hero = Hero('Mars')
    with pytest.raises(errors.TheSavingsInUndone):
        hero.savings_completed_at
