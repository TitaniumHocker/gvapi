# -*- coding: utf-8 -*-


class Pet:
    '''Класс питомца

    Данный класс описывает питомца.

    Args:
        hero (:py:class:`~gvapi.hero.Hero`): Экземпляр класса героя, которому принадлежит
            данный питомец.'''
    def __init__(self, hero):
        self.__hero = hero


    def __repr__(self) -> str:
        return '<Pet {}, class: {}>'.format(self.name, self.class_name)


    def __str__(self) -> str:
        return 'Питомец {} "{}"'.format(self.class_name, self.name)


    @property
    def name(self) -> str:
        '''str: Имя питомца.'''
        return self.__hero.data['pet']['pet_name']


    @property
    def class_name(self) -> str:
        '''str: Вид питомца.'''
        return self.__hero.data['pet']['pet_class']


    @property
    def level(self) -> int:
        '''int: Уровень питомца.'''
        return self.__hero.data['pet']['pet_level']


    @property
    def wounded(self) -> bool:
        '''bool: Контужен ли питомец.'''
        return self.__hero.data['pet'].get('wounded', False)
