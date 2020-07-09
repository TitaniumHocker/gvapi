Быстрый старт
=============

Установка
---------

Данный пакет доступен для установки из PyPi:

.. code-block:: bash

   python3 -m pip install gvapi


Также можно установить самую последнюю версию из репозитория:

.. code-block:: bash

   git clone https://github.com/TitaniumHocker/gvapi.git
   cd gvapi
   python3 -m pip install .

Пример использования
--------------------

Простейший пример использования будет выглядеть следующим образом.

.. literalinclude:: ../examples/simple.py
   :language: python

Данный скрипт выведет примерное количество золота героя и количество кирпичей.

.. code-block:: bash
   
   python3 simple.py
   ЗЛ: 8.0k, КП: 43.0%
