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
    "ark_f": 100,
    "ark_m": 100
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


class MockedResponse:
    status_code = 200

    @staticmethod
    def json():
        return BASE_HERO_DATA


class MockedResponseWithToken(MockedResponse):
    @staticmethod
    def json():
        return BASE_HERO_DATA_TOKEN


@pytest.fixture
def mocked_get():
    return lambda *args, **kwargs: MockedResponse()


@pytest.fixture
def mocked_get_t():
    return lambda *args, **kwargs: MockedResponseWithToken()


@pytest.fixture
def cli_runner():
    return CliRunner()
