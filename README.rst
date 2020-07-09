gvapi
=====

|python|
|coverage|
|version|
|requirements|
|doc|
|pypgk|

Неофициальная обертка для API игры `Годвилль <https://godville.net>`_, реализованная на Python.
`Документация <https://gvapi.readthedocs.io/ru/latest/>`_.

Установка
---------

Данный пакет доступен для установки из PyPi через ``pip``.

.. code-block:: bash

   python3 -m pip install gvapi


Пример использования
--------------------

Базовый вариант использования будет выглядеть следующим образом.

.. code-block:: python3

   from gvapi import Hero

   hero = Hero('God Name')
   hero_with_token = Hero('God Name', token='aiowdjwaoijd')

Описание атрибутов героя можно найти в документации.


.. |pypgk| image:: https://github.com/TitaniumHocker/gvapi/workflows/Python%20package/badge.svg?branch=master

.. |coverage| image:: https://raw.githubusercontent.com/TitaniumHocker/gvapi/master/media/coverage.svg

.. |python| image:: https://img.shields.io/badge/python-3.5%20|%203.6%20|%203.7%20|%203.8-blue?style=flat

.. |requirements| image:: https://img.shields.io/badge/requirements-requests%20%26%20click-blue?style=flat

.. |doc| image:: https://readthedocs.org/projects/gvapi/badge/?version=latest
   :target: https://gvapi.readthedocs.io/ru/latest/?badge=latest
   :alt: Documentation Status

.. |version| image:: https://badge.fury.io/py/gvapi.svg
   :target: https://badge.fury.io/py/gvapi
   :alt: Latest Version
