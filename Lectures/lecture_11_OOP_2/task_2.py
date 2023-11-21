"""Расширение неизменяемых классов"""


class NamedInt(int):
    """Класс int, где у каждого числа есть имя"""
    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        print(f'Создал класс {cls}')
        return instance


if __name__ == '__main__':
    print('Создаём первый раз')
    a = NamedInt(42, 'Главный ответ жизни, Вселенной и вообще')
    print('Создаём второй раз')
    b = NamedInt(73, 'Лучшее просто число')
    print(f'{a = }\t{a.name = }\t{type(a) = }')
    print(f'{b = }\t{b.name = }\t{type(b) = }')
    c = a + b
    print(f'{c = }\t{type(c) = }')
