# -*- coding: utf-8 -*-
"""В данном модуле расположены всякие штучки, в часности декораторы необходимые
для корректной работы классов :class:`~gvapi.Hero` и :class:`~gvapi.Pet`"""
from typing import Callable, Any
from functools import wraps
from gvapi import errors


def syncing(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Декоратор для принудительной синхронизации при вызове метода.

    При вызове метода, обернутого в данный декоратор, произойдет
    принудительный вызов метода `sync` класса переданного метода.

    :param func: декорируемый метод
    :return: метод, обернутый в декоратор"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        self.sync()
        return func(self, *args, **kwargs)
    return wrapper


def tokenized(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Декоратор для метода, требующего использования токена.

    При вызове метода, обернутого в данный декоратор, произойдет
    проверка на наличие токена в классе переданного метода.

    :param func: декорируемый метод
    :return: метод, обернутый в декоратор

    :raises :class:`~gvapi.errors.NeedToken`: в случае, если
    производится обращение к атрибуту, доступному только
    при использовании токена, без использования токена.
    :raises :class:`~gvapi.errors.InvalidToken`: в случае,
    если токен невалиден или был сброшен."""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.token:
            raise errors.NeedToken('Для доступа к данному атрибуту необходим токен. '
                                   'Получить токен: https://godville.net/user/profile')
        if 'health' not in self.data.keys():
            raise errors.InvalidToken(self.token)
        return func(self, *args, **kwargs)
    return wrapper
