# Создайте модуль с функцией внутри.
# � Функция принимает на вход три целых числа: нижнюю и
# верхнюю границу и количество попыток.
# � Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число
# попыток.
# � Функция выводит подсказки “больше” и “меньше”.
# � Если число угадано, возвращается истина, а если попытки
# исчерпаны - ложь.

from random import randint
from sys import argv


def guess_number(guesses: int, low_bound: int = 1,
                 upper_bound: int = 10) -> None:
    number = randint(low_bound, upper_bound)
    result = False
    while guesses > 0 and not result:
        user_num = int(input("Введите число: "))
        if user_num == number:
            result = True
        elif user_num > number:
            print('Меньше')
            guesses -= 1
        else:
            print('Больше')
            guesses -= 1
    if result:
        print("Вы победили")
    else:
        print("Вы проиграли")


if __name__ == '__main__':
    # guess_number(10, 20, 5)
    parsed_args = [int(arg) for arg in argv[1:]]
    guess_number(*parsed_args)
