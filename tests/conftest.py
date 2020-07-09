# -*- coding: utf-8 -*-
import pytest
from click.testing import CliRunner


BASE_HERO_DATA = {
    'name': 'Gaius Iulius Caesar',
    'godname': 'Mars',
    'gender': 'male',
    'level': 37,
    'max_health': 244,
    'inventory_max_num': 25,
    'motto': 'Какие-то букавы',
    'clan': 'Тестировщики',
    'clan_position': 'магистр',
    'alignment': 'добродушный',
    'bricks_cnt': 378,
    'pet': {
        'pet_name': 'Бублик «Обжора»',
        'pet_class': 'хохмяк',
        'pet_level':5
    },
    'ark_completed_at': None,
    'arena_won': 1,
    'arena_lost': 1,
    'inventory': {},
    'gold_approx': '',
    'ark_f': 100,
    'ark_m': 100
}


BASE_HERO_DATA_TOKEN = {
    'name': 'Gaius Iulius Caesar',
    'godname': 'Mars',
    'gender': 'male',
    'level': 37,
    'max_health': 244,
    'inventory_max_num': 25,
    'motto': 'Какие-то букавы',
    'clan': 'Тестировщики',
    'clan_position': 'магистр',
    'alignment': 'добродушный',
    'bricks_cnt': 379,
    'pet': {
        'pet_name': 'Бублик «Обжора»',
        'pet_class': 'хохмяк',
        'pet_level': 5
    },
    'ark_completed_at': None,
    'arena_won': 1,
    'arena_lost': 1,
    'health': 144,
    'quest_progress': 67,
    'exp_progress': 66,
    'godpower': 46,
    'gold_approx': 'около 3 сотен',
    'diary_last': 'Врач заверил, что с таким диагнозом мне не будет равных в психической атаке.',
    'town_name': 'Пустосвятово',
    'distance': 16,
    'arena_fight': False,
    'inventory_num': 14,
    'quest': 'разогнать парад планет (эпик)',
    'activatables': []
}


TOP_HERO_DATA = {
    **BASE_HERO_DATA,
    'temple_completed_at': '2015-11-01T01:48:51+03:00',
    'ark_completed_at': '2017-01-08T15:41:45+03:00',
    'savings_completed_at': '2020-05-14T17:37:51+03:00',
    'savings': '30000 тысяч',
    't_level': 18,
    'shop_name': 'Эволюция лайф',
    'boss_name': 'Обомлев',
    'boss_power': 211,
    'wood_cnt': 3456,
}


TOP_HERO_DATA_TOKEN = {
    **TOP_HERO_DATA,
    **BASE_HERO_DATA_TOKEN,
    'gold_approx': 'около тысячи'
}


class MockedResponse:
    status_code = 200

    @staticmethod
    def json():
        return BASE_HERO_DATA


class MockedResponseWithToken(MockedResponse):
    @staticmethod
    def json():
        return BASE_HERO_DATA_TOKEN


class MockedResponseTop(MockedResponse):
    @staticmethod
    def json():
        return TOP_HERO_DATA


class MockedResponseTopWithToken(MockedResponse):
    @staticmethod
    def json():
        return TOP_HERO_DATA_TOKEN


@pytest.fixture
def mocked_get():
    return lambda *args, **kwargs: MockedResponse()


@pytest.fixture
def mocked_get_t():
    return lambda *args, **kwargs: MockedResponseWithToken()


@pytest.fixture
def mocked_get_top():
    return lambda *args, **kwargs: MockedResponseTop()


@pytest.fixture
def mocked_get_top_t():
    return lambda *args, **kwargs: MockedResponseTopWithToken()


@pytest.fixture
def cli_runner():
    return CliRunner()
