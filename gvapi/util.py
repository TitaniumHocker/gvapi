# -*- coding: utf-8 -*-
from typing import Callable, Any
from functools import wraps
from gvapi import errors


def syncing(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
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


def tokenized(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
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
            raise errors.NeedToken('Для доступа к данному атрибуту необходим токен. '
                                   'Получить токен: https://godville.net/user/profile')
        if 'health' not in self.data.keys():
            raise errors.InvalidToken('Токен не действителен или был сброшен. Необходимо обновить.')
        return func(self, *args, **kwargs)
    return wrapper
