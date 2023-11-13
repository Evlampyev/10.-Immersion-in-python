"""Замыкания с неизменяемыми типами данных"""
from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    text = ''  # не изменяемый тип данных

    def add_two_str(b: str) -> str:
        nonlocal text  # команда nonlocal сообщает Python, что изменения ссылки
        # на объект должны затронуть область видимости за пределами функции add_two_str.
        text += ', ' + b
        return a + text

    return add_two_str


hello = add_one_str('Hello')
bye = add_one_str('Good bye')

print(hello('Alex'))
print(hello('Karina'))
print(bye('Alina'))
print(hello('John'))
print(bye('Neo'))
