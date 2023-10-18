# Решите квадратное уравнение 5x2-10x-400=0
# последовательно сохраняя переменные a, b, c, d, x1 и x2.
"""Решение квадратного уравнения"""
from math import sqrt

ratio_a, ratio_b, ratio_c = map(int, input("введите коэффициенты a, b, c: ").split())

discriminant = ratio_b * ratio_b - 4 * ratio_a * ratio_c
if discriminant < 0:
    result: str = "Корней нет"
elif discriminant == 0:
    x = -ratio_b / (2 * ratio_a)
    result = f"Один корень {x}"
else:
    x1 = (-ratio_b + sqrt(discriminant)) / (2 * ratio_a)
    x2 = (-ratio_b - sqrt(discriminant)) / (2 * ratio_a)
    result = f"Корни уравнения {x1} и {x2}"
print(result)
