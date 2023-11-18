# Создайте функцию-замыкание, которая запрашивает два целых числа:
# от 1 до 100 для загадывания,
# от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток
from random import randint


def ugadaika():
    n = randint(1, 100)
    count = 0
    while count not in range(1, 11):
        count = int(input("Введите количество попыток: "))

    def work_ugadaika():
        current_guess = 1
        while current_guess <= count:
            ans = int(input(f"Попытка №{current_guess}. Ваш вариант: "))
            if ans > n:
                print('Меньше')
            elif ans < n:
                print("Больше")
            else:
                print("Вы угадали!")
                break
            current_guess += 1
        else:
            print(f'Ваши попытки закончились. Вы проиграли. Ответ {n}.')

    return work_ugadaika


if __name__ == '__main__':
    my_func = ugadaika()
    my_func()
