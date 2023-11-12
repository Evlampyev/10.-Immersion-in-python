# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
from pathlib import Path
import pickle
import json


def search_json_file() -> list:
    """
    Поиск json файлов в директории
    :return: список файлов
    """
    all_json_files = []
    p = Path(Path.cwd())
    for file in p.iterdir():
        if file.is_file():
            file_name = file.name.rsplit('/')[-1]
            if file_name.rsplit('.')[-1] == 'json':
                all_json_files.append(file_name)
    return all_json_files


def json_to_picle(json_files: list):
    """Содержимое из json сохранить в pickle"""
    for file in json_files:
        with open(file, 'r', encoding='UTF-8') as json_file:
            data = json.load(json_file)
        only_name = file.split('.')[0]
        with open(f'{only_name}.picle', 'wb') as f:
            pickle.dump(data, f)


def main():
    json_to_picle(search_json_file())


if __name__ == '__main__':
    main()
