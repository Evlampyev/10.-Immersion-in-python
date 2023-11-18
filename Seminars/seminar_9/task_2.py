# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.
from random import randint
from typing import Callable


def ugadaika_decorator(func) -> Callable:
    """декоратор"""

    def wrapper(user_guess, user_num):
        """Обертка"""
        if user_num < 0 or user_num > 100:
            user_num = randint(1, 100)

        if user_guess not in range(1, 11):
            user_guess = randint(1, 10)
            print(f"Вы ввели не верное количество попыток, их будет: {user_guess}")
        result = func(user_guess, user_num)
        return result

    return wrapper


@ugadaika_decorator
def func_ugadaika(user_guess: int, user_num: int) -> str:
    """
    Угадываем число за указанное количество попыток
    :param user_guess: количество попыток
    :param user_num: загаданное число
    :return: результат угадывания
    """
    current_guess = 1
    while current_guess <= user_guess:
        ans = int(input(f"Попытка №{current_guess}. Ваш вариант: "))
        if ans > user_num:
            print('Меньше')
        elif ans < user_num:
            print("Больше")
        else:
            return f"Вы угадали на {current_guess} попытке. "
        current_guess += 1
    else:
        return f'Ваши попытки закончились. Вы проиграли. Ответ {user_num}.'


if __name__ == '__main__':
    step = int(input("Введите количество попыток: "))
    number = randint(1, 200)

    my_func = func_ugadaika(step, number)
    print(my_func)
