"""Декоратор wraps"""

import time
from typing import Callable
from functools import wraps


def count(num: int = 1):
    """
    Внешняя функция декоратора
    :param num: будет использован для цикла fo
    :return:
    """

    def deco(func: Callable):
        """
        Получение функции для декорирования
        :param func: декларируемая функция
        :return:
        """

        @wraps(func)  # позволяет сохранить строку документации и имя функции,
        # передаваемой в декоратор
        def wrapper(*args, **kwargs):
            """
            внутренняя функция декоратора
            :param args:
            :param kwargs:
            :return:
            """
            time_for_count = []  # для хранения результатов замеров быстродействия
            result = None
            for _ in range(num):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                stop = time.perf_counter()
                time_for_count.append(stop - start)
            print(f'Результаты замеров {time_for_count}')
            return result

        return wrapper

    return deco


@count(10)  # Запускаем цикл for столько раз, сколько мы передали в декоратор:
def factorial(n: int) -> int:
    """Returns the factorial of the number n."""
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(1000) = }')
print(f'{factorial(1000) = }')
help(factorial)
