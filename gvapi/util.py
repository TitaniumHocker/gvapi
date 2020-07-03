# -*- coding: utf-8 -*-
from functools import wraps
from gvapi import errors


def syncing(func):
    '''Декоратор для принудительной синхронизации при вызове функции.'''
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        self.sync()
        return func(self, *args, **kwargs)
    return wrapper


def tokenized(func):
    '''Декоратор для функций, требующих использования токена.'''
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.token:
            raise errors.NeedToken('Для доступа к данному атрибуту необходим токен.')
        if 'health' not in self.raw_data.keys():
            raise errors.TokenWasResetted('Токен был сброшен, необходимо обновить токен.')
        return func(self, *args, **kwargs)
    return wrapper
