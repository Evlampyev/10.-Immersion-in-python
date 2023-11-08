# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform
import os


def write_num_in_file(count: int, file_name: str) -> None:
    if not os.path.exists(file_name):
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write("")
    else:
        with open(file_name, 'a') as file:
            for i in range(count):
                int_num = randint(-10000, 1000)
                float_num = uniform(-1000, 1000)
                row = f'{int_num} | {float_num} \n'
                file.write(row)


if __name__ == '__main__':
    write_num_in_file(5, 'new_file.txt')
