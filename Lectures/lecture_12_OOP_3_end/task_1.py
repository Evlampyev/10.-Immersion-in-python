"""Вызов экземпляра класса как функцию"""

from collections import defaultdict


# При обращении к defaultdict по несуществующему ключу не будет ошибки, как у обычного словаря, а вернется пустой список


class Storage:
    """Хранилище"""
    def __init__(self):
        self.storage = defaultdict(list)

    def __str__(self):
        txt = '\n'.join((f'{k}: {v}' for k, v in self.storage.items()))
        return f'Объекты хранилища по типам:\n{txt}'

    def __call__(self, value):
        """Вызывает экземпляр класса как функцию с передаваемым значением value"""
        self.storage[type(value)].append(value)
        return f'К типу {type(value)} добавлен {value}'


if __name__ == '__main__':
    s = Storage()
    print(s(42))
    print(s(72))
    print(s('Hello world!'))
    print(s(0))
    print(s)
