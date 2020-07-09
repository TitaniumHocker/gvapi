# -*- coding: utf-8 -*-
from urllib.parse import quote
from datetime import datetime
import json
import requests

from gvapi.util import syncing, tokenized
from gvapi import errors
from gvapi.pet import Pet


class Hero:
    '''Основной класс пакета.

    Через данный класс осуществляется доступ к данным героя.

    Attributes:
        god (str): Имя бога.
        base_url (str): URL для доступа к API.
        data (dict): Словарь с последними полученными данными.
        pet (:py:class:`~gvapi.pet.Pet`): Экземпляр класса `Pet`, описывающий питомца.

    Arguments:
        god (str): Имя бога.
        token (str, optional): Токен для доступа к API. Если не указан,
            то обращение производится к открытому API.
        api_url (str, optional): URL для доступа к API. Если не указан,
            то используется `https://godville.net/gods/api`.
        threshold (int, optional): Задержка обновления данных о герое в секундах,
            по умолчанию 300 секунд или 5 минут. Данный параметр не может быть меньше 60(1 минута).
    '''
    def __init__(self, god, token=None, api_url='https://godville.net/gods/api', threshold=300):
        if threshold < 60:
            raise errors.MinThresholdException('Параметр threshold не может быть меньше 60 секунд.')
        self.__token = token
        self.__threshold = threshold
        self.__last_upd = datetime.now()
        self.__lock = False
        self.base_url = api_url
        self.god = god
        self.data = self.__get_data()
        self.pet = Pet(self)


    def __repr__(self):
        return '<Hero {}>'.format(self.name)


    def __str__(self):
        if self.gender == 'муж':
            return 'Герой {}'.format(self.name)
        return 'Героиня {}'.format(self.name)


    @property
    def last_upd(self):
        ''':py:class:`datetime`: Время последнего обновления данных.'''
        return self.__last_upd


    @property
    def lock(self):
        '''bool: Заблокированы ли запросы к API.'''
        return self.__lock


    def sync(self):
        '''Синхронизировать данные

        Произвести синхронизацию данных.
        Синхронизация производится только в случае если прошла
        задержка обновления данных(`threshold`).
        '''
        if self.from_last_updated > self.threshold and not self.lock:
            self.data = self.__get_data()
            self.__last_upd = datetime.now()


    def __get_data(self):
        '''Получить данные.

        Произвести обращение к API для получения данных о герое.

        Returns:
            Словать с данными полученными от API.

        Raises:
            :py:class:`~gvapi.errors.APIUnavailable`
                в случае недоступности API.

            :py:class:`~gvapi.errors.UnexpectedAPIResponse`
                в случае получения неожиданного ответа от API.
        '''
        self.__lock = True

        if self.__token:
            url = '{}/{}/{}'.format(self.base_url, quote(self.god, safe=''), self.__token)
        else:
            url = '{}/{}'.format(self.base_url, quote(self.god, safe=''))

        try:
            response = requests.get(url)
        except (requests.ConnectTimeout, requests.ConnectionError) as exc:
            raise errors.APIUnavailable('Обращение к API закончилось неудачей: {}'.format(exc))

        if response.status_code != 200:
            raise errors.UnexpectedAPIResponse(
                'Неожиданный ответ API(код {}) :{}'.format(response.status_code, response.text)
            )

        try:
            data = response.json()
        except json.decoder.JSONDecodeError:
            raise errors.UnexpectedAPIResponse(
                'Неожиданный ответ API(код {}) :{}'.format(response.status_code, response.text)
            )

        self.__lock = False
        return data


    @property
    def threshold(self):
        '''int: Задержка обновления данных о герое в секундах.'''
        return self.__threshold


    @threshold.setter
    def threshold(self, time):
        if time < 60:
            raise errors.MinThresholdException('Параметр threshold не может быть меньше 60 секунд.')
        self.__threshold = time


    @property
    def from_last_updated(self):
        '''int: Количество секунд, прошедших с последнего обновления данных.'''
        return int(datetime.now().timestamp() - self.__last_upd.timestamp())


    @property
    def token(self):
        '''str: Токен в защищенном формате(не скрыты только последние 4 символа).
            Если токен не используется, то возвращает `None`'''
        if not self.__token:
            return None
        return '{}{}'.format('*' * len(self.__token[:-4:]), self.__token[-4::])


    @property
    @syncing
    def name(self):
        '''str: Имя героя.'''
        return self.data['name']


    @property
    @syncing
    def gender(self):
        '''str: Пол героя.'''
        return 'муж' if self.data['gender'] == 'male' else 'жен'


    @property
    @syncing
    @tokenized
    def is_alive(self):
        '''bool: Жив ли герой.'''
        return self.health > 0


    @property
    @syncing
    @tokenized
    def health(self):
        '''int: Количество очков здоровья героя.'''
        return self.data['health']


    @property
    @syncing
    def max_health(self):
        '''int: Максимальное количество очков здоровья героя.'''
        return self.data['max_health']


    @property
    @syncing
    @tokenized
    def health_percent(self):
        '''float: Количество очков здоровья героя в процентах.'''
        return self.health / self.max_health


    @property
    @syncing
    @tokenized
    def gold(self):
        '''str: Примерное количество золота.'''
        return self.data['gold_approx']


    @property
    @syncing
    @tokenized
    def goldf(self):
        '''float: Приверное количество золота, отформатированное в тысячи.'''
        words = self.gold.split()[1::]
        mul = 1 if words[-1].startswith('тыс') else 0.1
        if len(words) == 1:
            return 1.0 * mul
        return float(words[0]) * mul



    @property
    @syncing
    @tokenized
    def activatables(self):
        '''list: Список активируемых предметов.'''
        return self.data['activatables']


    @property
    @syncing
    @tokenized
    def is_fighting(self):
        '''bool: Находится ли герой в бою(арена, босс, заплыв, подземка).'''
        return self.data['arena_fight']


    @property
    @syncing
    @tokenized
    def fight_type(self):
        '''str: Тип боя'''
        return self.data['fight_type'] if self.is_fighting else ''


    @property
    @syncing
    @tokenized
    def aura(self):
        '''str: Аура, если отсутствует - пустая строка'''
        return self.data.get('aura', '')


    @property
    @syncing
    @tokenized
    def diary_last(self):
        '''str: Последняя запись в дневнике.'''
        return self.data['diary_last']


    @property
    @syncing
    @tokenized
    def distance(self):
        '''int: Дистанция до столицы, при нахождении в любом городе - 0.'''
        return self.data['distance']


    @property
    @syncing
    @tokenized
    def exp(self):
        '''int: Прогресс опыта.'''
        return self.data['exp_progress']


    @property
    @syncing
    @tokenized
    def expired(self):
        '''bool: Флаг актуальности данных, True в случае, когда данные неакутальны.'''
        return self.data.get('expired', False)


    @property
    @syncing
    @tokenized
    def godpower(self):
        '''int: Количество праны.'''
        return self.data['godpower']


    @property
    @syncing
    def max_godpower(self):
        '''int: Максимальное количество праны.'''
        return 200 if self.data.get('savings_completed_at', None) else 100


    @property
    @syncing
    @tokenized
    def godpower_percent(self):
        '''int: Количество праны в процентах.'''
        return self.godpower / self.max_godpower


    @property
    @syncing
    @tokenized
    def inventory_num(self):
        '''int: Количество предметов в инвентаре.'''
        return self.data['inventory_num']


    @property
    @syncing
    def inventory_max_num(self):
        '''int: Максимальное количество предметов в инвентаре.'''
        return self.data['inventory_max_num']


    @property
    @syncing
    @tokenized
    def inventory(self):
        '''tuple: Корнеж из количества предметов в инвентаре, максимального количества предметов
            и количества активируемых предметов.'''
        return (self.inventory_num, self.inventory_max_num, self.activatables)


    @property
    @syncing
    @tokenized
    def quest_progress(self):
        '''float: Процесс выполнения задания в процентах.'''
        return self.data.get('quest_progress', 0.0)


    @property
    @syncing
    @tokenized
    def quest(self):
        '''str: Текст текущего задания.'''
        return self.data.get('quest', '')


    @property
    @syncing
    @tokenized
    def town_name(self):
        '''str: Имя города, пустая строка если в поле или в бою.'''
        return self.data.get('town_name', '')


    @property
    @syncing
    def words(self):
        '''int: Количество слов в книге.'''
        return self.data.get('words', 0)


    @property
    @syncing
    def ark(self):
        '''tuple: Число тварей(ж, м)'''
        if not self.data.get('ark_f', None):
            raise errors.TheArkIsUndone('Ковчег еще не достроен.')
        return (self.data['ark_f'], self.data['ark_m'])


    @property
    @syncing
    def savings(self):
        '''str: Примерное число сбережений.'''
        if not self.data.get('temple_completed_at', None):
            raise errors.TheTempleIsUndone('Храм еще не построен.')
        return self.data['savings']


    @property
    @syncing
    def t_level(self):
        '''int: Троговый уровень.'''
        if not self.data.get('savings_completed_at', None):
            raise errors.TheSavingsInUndone('Пенсия еще не собрана.')
        return self.data.get('t_level', 0)


    @property
    @syncing
    def arena(self):
        '''tuple: число побед и поражений на арене.'''
        return (self.data['arena_won'], self.data['arena_lost'])


    @property
    @syncing
    def ark_completed_at(self):
        '''str: Дата постройки ковчега.'''
        if not self.data.get('ark_completed_at', None):
            raise errors.TheArkIsUndone('Ковчег еще не построен.')
        return self.data['ark_completed_at']


    @property
    @syncing
    def alignment(self):
        '''str: Характер героя.'''
        return self.data['alignment']


    @property
    @syncing
    def bricks(self):
        '''int: Число кирпичей для храма.'''
        return self.data['bricks_cnt']


    @property
    @syncing
    def bricks_percent(self):
        '''float: Число кирпичей для храма в процентах.'''
        return self.data['bricks_cnt'] / 1000 * 100


    @property
    @syncing
    def clan(self):
        '''str: Название гильдии героя.'''
        return self.data['clan']


    @property
    @syncing
    def clan_pos(self):
        '''str: Ранг героя в гильдии.'''
        return self.data['clan_position']


    @property
    @syncing
    def level(self):
        '''int: Уровень героя.'''
        return self.data['level']


    @property
    @syncing
    def motto(self):
        '''str: Девиз героя.'''
        return self.data.get('motto', '')


    @property
    @syncing
    def savings_completed_at(self):
        '''str: Дата окончания сбора пенсии.'''
        if not self.data.get('savings_completed_at', None):
            raise errors.TheSavingsInUndone('Сбережения еще не собраны.')
        return self.data['savings_completed_at']


    @property
    @syncing
    def shop_name(self):
        '''str: Название лавки, только у пенсионеров.'''
        if not self.data.get('savings_completed_at', None):
            raise errors.TheSavingsInUndone('Сбережения еще не собраны.')
        return self.data.get('shop_name', '')


    @property
    @syncing
    def temple_completed_at(self):
        '''str: Когда был достроен храм.'''
        if not self.data.get('temple_completed_at', None):
            raise errors.TheTempleIsUndone('Храм еще не построен.')
        return self.data['temple_completed_at']


    @property
    @syncing
    def wood_count(self):
        '''int: Количество поленьев.'''
        if not self.data.get('temple_completed_at', None):
            raise errors.TheTempleIsUndone('Храм еще не построен.')
        return self.data['wood_cnt']


    @property
    @syncing
    def boss_name(self):
        '''str: Имя собранного в лаборатории босса.'''
        return self.data.get('boss_name', None)


    @property
    @syncing
    def boss_power(self):
        '''str: Мощь собранного в лаборатории босса.'''
        return self.data.get('boss_power', None)
