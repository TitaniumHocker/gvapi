# -*- coding: utf-8 -*-


class Pet:
    '''Класс питомца

    Описывает питомца.

    Attributes:
        __hero (:py:class:`~gvapi.hero.Hero`): Экземпляр класса героя, которому принадлежит
            данный питомец.

    Args:
        hero (:py:class:`~gvapi.hero.Hero`): Экземпляр класса героя, которому принадлежит
            данный питомец.'''
    def __init__(self, hero):
        self.__hero = hero


    def __repr__(self):
        return '<Pet {}, class: {}>'.format(self.name, self.class_name)


    def __str__(self):
        return 'Питомец {} "{}"'.format(self.class_name, self.name)


    @property
    def name(self):
        '''str: Имя питомца.'''
        return self.__hero._data['pet']['pet_name']


    @property
    def class_name(self):
        '''str: Вид питомца.'''
        return self.__hero._data['pet']['pet_class']


    @property
    def level(self):
        '''int: Уровень питомца.'''
        return self.__hero._data['pet']['pet_level']


    @property
    def wounded(self):
        '''bool: Контужен ли питомец.'''
        return self.__hero._data['pet'].get('wounded', False)
