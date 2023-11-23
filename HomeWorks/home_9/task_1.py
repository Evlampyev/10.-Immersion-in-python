from random import randint
import csv
from math import sqrt
from typing import Callable
import json

JSON_RESULT_FILE = 'results.json'


def generate_csv_file(file_name: str, rows: int):
    """Генерирует по три случайных числа в каждой строке, от 100-1000 строк
    :param file_name: имя файла
    :param rows: количество строк
    :return: None
    """
    with open(file_name, 'w', newline='', encoding='UTF-8') as f_write:
        csv_write = csv.writer(f_write, dialect='excel', delimiter=' ')
        all_data = []
        for row in range(rows):
            num_list = []
            for _ in range(3):
                num = randint(-10, 10)
                num_list.append(num)
            all_data.append(num_list)
        csv_write.writerows(all_data)


def save_to_json(func) -> Callable:
    def wrapper(*args):
        input_file_name = args[0]
        all_data = {}
        with (open(input_file_name, 'r', newline='', encoding='UTF-8') as f_read,
              open(JSON_RESULT_FILE, 'w', encoding='UTF-8') as f_write
              ):
            csv_file = csv.reader(f_read)
            key = 1
            for line in csv_file:
                a, b, c = map(int, line[0].split())
                result = func(a, b, c)
                all_data[key] = {'a': a, 'b': b, 'c': c, 'result': result}
                key += 1
            json.dump(all_data, f_write, indent=4)

    return wrapper


@save_to_json
def find_roots(a: int, b: int, c: int):
    """Возвращает корни квадратного уравнения
    :param a: коэффициент a
    :param b: коэффициент b
    :param c: коэффициент c
    :return: список корней
    """
    d = b * b - 4 * a * c
    if a == 0:
        if b == 0:
            if c == 0:
                return 'all x'
            else:
                return None
        else:
            return -c / b
    else:
        if d < 0:
            return None
        elif d == 0:
            return -b / (2 * a)
        else:
            x1 = (-b + sqrt(d)) / (2 * a)
            x2 = (-b - sqrt(d)) / (2 * a)
            return x1, x2


if __name__ == '__main__':
    generate_csv_file("input_data.csv", 101)
    find_roots("input_data.csv")

    with open("results.json", 'r') as f:
        data = json.load(f)

    if 100 <= len(data) <= 1000:
        print(True)
    else:
        print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

    print(len(data) == 101)
