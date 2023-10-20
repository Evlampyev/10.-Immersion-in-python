"""Квадратное уровнение в комплексных числах"""
from math import sqrt

a, b, c = 7, 5, 2
discr = b ** 2 - 4 * a * c
result = None
if discr > 0:
    x1 = (-b + sqrt(discr)) / (2 * a)
    x2 = (-b - sqrt(discr)) / (2 * a)
    result = [x1, x2]
elif discr == 0:
    x = -b / (2 * a)
    result = x
else:
    x1 = -b + (discr * 1j) ** 2 / (2 * a)
    x2 = -b - (discr * 1j) ** 2 / (2 * a)
    result = [x1, x2]
print(result)
