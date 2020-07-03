# -*- coding: utf-8 -*-
'''Модуль с исключениями.

В данном модуле описаны исключения, использующиеся в пакете.'''


class GVAPIException(Exception):
    '''Общее исключение пакета.'''


class APIUnavailable(GVAPIException):
    '''API недоступно.'''


class UnexpectedAPIResponse(GVAPIException):
    '''Непредвиденный ответ API.'''


class TokenWasResetted(GVAPIException):
    '''Токен был сброшен и требует обновления.'''


class NeedToken(GVAPIException):
    '''Для доступа необходим токен.'''


class TheTempleIsUndone(GVAPIException):
    '''Храм еще не построен.'''


class TheArkIsUndone(GVAPIException):
    '''Ковчег еще не построен.'''


class TheSavingsInUndone(GVAPIException):
    '''Сбережения(пенсия) еще не собраны.'''


class MinThresholdException(GVAPIException):
    '''Порог обновления меньше минимального значения.'''
