"""Замыкания с изменяемыми типами данных"""
from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    names = []  # изменяемый тип данных

    def add_two_str(b: str) -> str:
        names.append(b)
        return a + ', ' + ', '.join(names)

    return add_two_str


hello = add_one_str('Hello')
bye = add_one_str('Good bye')

# У каждой из двух функций hello и bye оказывается свой список names.
# Они не связаны между собой, но каждый хранит список имён до конца работы программы.

print(hello('Alex'))
print(hello('Karina'))
print(bye('Alina'))
print(hello('John'))
print(bye('Neo'))
