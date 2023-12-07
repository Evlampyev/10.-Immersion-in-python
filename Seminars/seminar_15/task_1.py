# Напишите программу, которая использует модуль logging для вывода сообщения
# об ошибке в файл. 📌 Например отлавливаем ошибку деления на ноль.

from logging import WARNING, basicConfig, getLogger
from typing import Any


def get_from_dict(dct: dict, key: Any):
    try:
        return dct[key]
    except KeyError as e:
        LOGGER.critical(f'Cannot get value from key: {key}, {e}')


if __name__ == '__main__':
    basicConfig(filename='log/log_1.log', level=WARNING, datefmt='%H:%M:%S',
                format='[{levelname:<8}] {asctime}: {msg}', style='{')
    LOGGER = getLogger(__name__)

    dct = {
        1: 'one',
        2: 'two',
        3: 'three'
    }

    get_from_dict(dct, 4)
