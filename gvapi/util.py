# -*- coding: utf-8 -*-
from functools import wraps
from gvapi import errors


def syncing(func):
    '''Декоратор для принудительной синхронизации при вызове метода.

    Args:
        func (func): Декорируемая функция.

    Returns:
        func : Функция, обернутая в декоратор.
    '''
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        self.sync()
        return func(self, *args, **kwargs)
    return wrapper


def tokenized(func):
    '''Декоратор для метода, требующего использования токена.

    Args:
        func (func): Декорируемая функция.

    Returns:
        func : Функция, обернутая в декоратор.

    Raises:
        :py:class:`~gvapi.errors.NeedToken`
            в случае, если производится обращение к атрибуту, доступнопу только при использовании
            токена, без использования токена.

        :py:class:`~gvapi.errors.TokenWasResetted`
            в случае, если токен был сброшен.
        '''
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.token:
            raise errors.NeedToken('Для доступа к данному атрибуту необходим токен.')
        if 'health' not in self.data.keys():
            raise errors.TokenWasResetted('Токен был сброшен, необходимо обновить токен.')
        return func(self, *args, **kwargs)
    return wrapper
