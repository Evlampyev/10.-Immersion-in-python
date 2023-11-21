"""Шаблон Одиночка = Singleton"""


class Singleton:
    """Класс у которого только один экземпляр класса"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        """Контроль создания только одного экземпляра класса"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name: str):
        """
        Добавляет параметр при создании экземпляра класса
        :param name: имя
        """
        self.name = name


if __name__ == '__main__':
    a = Singleton('Первый')
    print(f'{a.name = }')
    b = Singleton('Второй')
    print(f'{a is b = }')
    print(f'{a.name = }\n{b.name = }')

    # работа с документацией класса и экземпляра класса
    print('Справка класса Singleton ниже', '*' * 50)
    help(Singleton)
    print('Справка экземпляра a ниже', '*' * 50)
    help(a)

    print(f'Документация класса: {Singleton.__doc__ = }')
    print(f'Документация экземпляра: {a.__doc__ = }')
    print(f'Документация метода: {a.__new__.__doc__}')
