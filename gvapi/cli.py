# -*- coding: utf-8 -*-
'''Модуль, описывающий CLI-утилиту пакета gvapi'''
import sys
from os import environ
from pathlib import Path
from hashlib import md5
import pickle
import click
from gvapi import Hero, errors


@click.command()
@click.option('-g', '--god', required=False, default=environ.get('GVAPI_GOD'), help='Имя божества')
@click.option('-t', '--token', required=False, default=environ.get('GVAPI_TOKEN'), help='Токен')
@click.option('--drop-cache', is_flag=True, default=False, help='Сбросить кэш при выполнении')
@click.argument('property_name', required=True)
def cli(god, token, drop_cache, property_name):
    '''CLI-интерфейс для доступа к API игры Годвилль.

    Аргументы:

        PROPERTY_NAME Имя свойства героя

    Полный список свойств и примеры использования данного
    CLI-интерфейса можно получить в документации.'''
    if not god:
        raise errors.GVAPIException('Не получено имя божества.')

    cache_dir = Path(Path.joinpath(Path.home(), '.cache', 'gvapi'))
    cache_dir.mkdir(parents=True, exist_ok=True)

    if token:
        cache_filename = md5('{}:{}'.format(god, token).encode()).hexdigest()
    else:
        cache_filename = md5(god.encode()).hexdigest()

    cache = Path(Path.joinpath(cache_dir, cache_filename))

    if cache.is_file() and not drop_cache:
        with open(cache, 'rb') as dump:
            hero = pickle.loads(dump.read())
    else:
        if token:
            hero = Hero(god, token)
        else:
            hero = Hero(god)

    try:
        value = getattr(hero, property_name)
    except AttributeError:
        click.echo("Получено некорректное свойство {}".format(property_name))
        sys.exit(1)
    except errors.NeedToken:
        click.echo('Для доступа к данному свойству необходим токен')
        sys.exit(1)
    except errors.InvalidToken:
        click.echo("Токен невалиден или был сброшен")
        sys.exit(1)
    click.echo(value)

    with open(cache, 'wb') as dump:
        dump.write(pickle.dumps(hero))
