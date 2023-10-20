"""Задача_3"""

# Напишите программу, которая вычисляет площадь круга и длину окружности
# по введённому диаметру.
# ✔Диаметр не превышает 1000 у.е.
# ✔Точность вычислений должна составлять не менее 42 знаков

import decimal
import math

decimal.getcontext().prec = 50

radius = decimal.Decimal(input('Введите диаметр: ')) / 2
a = decimal.Decimal(math.pi) * radius ** 2
print(a)
print(len(str(a)))
