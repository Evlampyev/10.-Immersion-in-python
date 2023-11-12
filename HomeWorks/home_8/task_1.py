# Ваша задача - написать программу, которая принимает на вход директорию и
# рекурсивно обходит эту директорию и все вложенные директории.
# Результаты обхода должны быть сохранены в нескольких форматах: JSON, CSV и Pickle.
# Каждый результат должен содержать следующую информацию:
# Путь к файлу или директории: Абсолютный путь к файлу или директории.
# Тип объекта: Это файл или директория.
# Размер: Для файлов - размер в байтах, для директорий - размер,
# учитывая все вложенные файлы и директории в байтах.


import json
import csv
import pickle
from pathlib import Path
import os


def traverse_directory(directory: str) -> list[dict]:
    """
    Выполняет обход директории и возвращать результаты в виде списка словарей
    :param directory:  рабочий директорий
    :return: список словарей
    """
    my_list = []
    for dir_path, dir_name, file_name in os.walk(os.getcwd()):
        # dict = {'path': dir_path, 'type': }
        print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')


def save_results_to_json(all_files: list[dict]):
    """Сохранение списка словарей в JSON"""
    pass


def save_results_to_csv(all_files: list[dict]):
    """Сохранение списка словарей в CSV """
    pass


def save_results_to_picle(all_files: list[dict]):
    """Сохранение списка словарей в PICLE"""
    pass


def main():
    my_dir = '/home_8'
    traverse_directory(my_dir)


if __name__ == '__main__':
    main()
