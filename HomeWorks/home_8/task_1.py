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
import os


def get_dir_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
        for d in dirnames:
            dp = os.path.join(dirpath, d)
            total_size += get_dir_size(dp)
    return total_size


def save_results_to_json(results, file_name):
    """Сохранение списка словарей в JSON"""
    with open(file_name, 'w') as f:
        json.dump(results, f)


def save_results_to_csv(results, file_name):
    """Сохранение списка словарей в CSV """
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Path', 'Type', 'Size'])
        for result in results:
            writer.writerow([result['Path'], result['Type'], result['Size']])


def save_results_to_picle(results, file_name):
    """Сохранение списка словарей в PICLE"""
    with open(file_name, 'wb') as f:
        pickle.dump(results, f)


def traverse_directory(directory: str) -> list[dict]:
    """
    Выполняет обход директории и возвращать результаты в виде списка словарей
    :param directory:  рабочий директорий
    :return: список словарей
    """
    results = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            results.append({'Path': path, 'Type': 'File', 'Size': size})
        for name in dirs:
            path = os.path.join(root, name)
            size = get_dir_size(path)
            results.append({'Path': path, 'Type': 'Directory', 'Size': size})
    return results


def main():
    my_dir = '/HomeWorks/home_8'
    print(traverse_directory(my_dir))


if __name__ == '__main__':
    main()
