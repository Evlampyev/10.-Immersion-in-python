"""Дополнительные модули """
from math import gcd  # математический модуль
from decimal import Decimal, getcontext  # для увеличения точности вещественных чисел
from fractions import Fraction  # для работы с дробями с точностью

getcontext().prec = 35  # задание точности, количества знаков после запятой
pi = Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375')
print(pi)
print(2 * Decimal(pi) * 15 ** 2)

f1 = Fraction(1, 3)
f2 = Fraction(2, 3)

print(f"{f1} + {f2} = {f1 + f2}")

a: int = 24
b: int = 48
c: int = 1024
print(gcd(a, b, c))  # Находит наибольший общий делитель
