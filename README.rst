gvapi
=====

|python|
|coverage|
|version|
|requirements|
|pypgk|

Неофициальная обертка для API игры `Годвилль <https://godville.net>`_, реализованная на Python.
`Документация <https://gvapi.readthedocs.io/en/latest/>`_.

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

.. |coverage| image:: https://img.shields.io/badge/coverage-92%25-green?style=flat-square

.. |version| image:: https://img.shields.io/badge/version-0.2-red?style=flat-square

.. |python| image:: https://img.shields.io/badge/python-3.5%20|%203.6%20|%203.7%20|%203.8-blue?style=flat-square

.. |requirements| image:: https://img.shields.io/badge/requirements-requests%20%26%20click-blue?style=flat-square
