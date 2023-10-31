# Создайте функцию-генератор.
# Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте правило:
# «число является простым, если делится нацело только на единицу и на себя».
from math import sqrt


def is_prime(num: int) -> bool:
    """Проверка числа на простоту"""
    result: bool = True
    if num % 2 == 0:
        result = False
    i: int = 3
    while result and i <= int(sqrt(num)):
        if num % i == 0:
            result = False
        i += 2
    return result


def my_gen(n: int):
    """Генератор простых чисел"""
    yield 2
    n -= 1
    i: int = 3
    while n > 0:
        if is_prime(i):
            n -= 1
            yield i
            i += 1
        else:
            i += 1


for next_prime in my_gen(10):
    print(next_prime)
