# -*- coding: utf-8 -*-
'''Модуль, описывающий CLI-утилиту пакета gvapi'''
from os import environ
import click

from gvapi import Hero


@click.group()
@click.option('--verbose', is_flag=True, default=False, help='Запуск в режиме отладки.')
@click.pass_context
def cli(ctx, verbose):
    '''CLI-интерфейс для доступа к API игры Годвилль.'''
    ctx.ensure_object(dict)
    ctx.obj['verbose'] = verbose


if __name__ == '__main__':
    cli(obj={})
