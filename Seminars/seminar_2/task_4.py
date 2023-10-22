"""Квадратное уравнение в комплексных числах"""
from math import sqrt
from cmath import sqrt as c_sqrt

# a, b, c = 1, - 4, 5
a, b, c = 0, 2, -1
discr: int = b ** 2 - 4 * a * c
result: float | list = None
if a == 0:
    x: float = -c / b
    result: float = x
elif discr > 0:
    x1 = (-b + sqrt(discr)) / (2 * a)
    x2 = (-b - sqrt(discr)) / (2 * a)
    result = [x1, x2]
elif discr == 0:
    x: float = -b / (2 * a)
    result: float = x
else:
    x1 = (-b + c_sqrt(discr)) / (2 * a)
    x2 = (-b - c_sqrt(discr)) / (2 * a)
    result = [x1, x2]
print(result)
