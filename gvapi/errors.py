# -*- coding: utf-8 -*-
'''Модуль с исключениями.

В данном модуле описаны исключения, использующиеся в пакете.'''
from requests import Response


class GVAPIException(Exception):
    '''Общее исключение пакета.
    От данного исключения наследуются остальные исключения пакета.
    '''

class UnknownGod(GVAPIException):
    '''Бог не был найден.'''
    def __init__(self, god: str, message: str = 'Божество {} не было найдено.'):
        self.god = god
        self.message = message.format(self.god)
        super().__init__(self.message)


class APIUnavailable(GVAPIException):
    '''API недоступно.'''
    def __init__(self, exc: Exception,  message: str = 'API Недоступно {}'):
        self.message = message.format(exc)
        super().__init__(self.message)


class UnexpectedAPIResponse(GVAPIException):
    '''Непредвиденный ответ API.'''
    def __init__(self, resp: Response, message: str = 'Непредвиденный ответ API {}: {}'):
        self.resp = resp
        self.messsage = message.format(resp.status_code, resp.text)
        super().__init__(self.messsage)


class InvalidToken(GVAPIException):
    '''Токен невалилен или был сброшен.'''
    def __init__(self, token: str, message: str = 'Токен {} невалиден или был сброшен'):
        self.token = token
        self.message = message.format(token)
        super().__init__(self.message)


class NeedToken(GVAPIException):
    '''Для доступа необходим токен.'''
    def __init__(self, message: str = 'Для доступа к данному атрибуту необходим токен'):
        self.message = message
        super().__init__(self.message)


class TheTempleIsUndone(GVAPIException):
    '''Храм еще не построен.'''


class TheArkIsUndone(GVAPIException):
    '''Ковчег еще не построен.'''


class TheSavingsInUndone(GVAPIException):
    '''Сбережения(пенсия) еще не собраны.'''


class MinThresholdException(GVAPIException):
    '''Порог обновления меньше минимального значения.'''
