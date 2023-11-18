# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции.
from typing import Callable


def count_calls(calls: int) -> Callable:
    def my_func_decorator(func: Callable) -> Callable:
        result = []

        def wrapper(*args):
            nonlocal result  # не местная переменная
            current_call = 0
            while current_call < calls:
                result.append(func(*args))
                current_call += 1
            return result

        return wrapper

    return my_func_decorator


@count_calls(5)
def my_function(*args):
    my_sum = 0
    for arg in args:
        my_sum += arg
    return my_sum


if __name__ == '__main__':
    for i in range(1, 5):
        my_func = my_function(i, i + i, i * i)
        print(my_func)
