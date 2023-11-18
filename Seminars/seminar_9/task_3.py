# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает.
# При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.
import json
import os.path
from random import randint
from typing import Callable


def decorator_save_to_json(func) -> Callable:
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        file_name = func_name + '.json'
        print(f'{file_name = }')
        if not os.path.exists(file_name):
            with open(file_name, 'w', encoding='UTF-8') as f:
                json.dump({}, f)

        with open(file_name, 'r', encoding='UTF-8') as f:
            data = dict(json.load(f))

        print(f'{data = }')
        result = func(*args, **kwargs)
        data[result] = {'args': args}
        for key, value in kwargs.items():
            data[result][key] = value
        with open(file_name, 'w', encoding='UTF-8') as f:
            json.dump(data, f, ensure_ascii=False)

        return result

    return wrapper


@decorator_save_to_json
def function(*args, **kwargs) -> int:
    """Возведение числа в степень"""
    number, number_pow = args[0], args[1]
    return pow(number, number_pow)


if __name__ == '__main__':
    num = randint(2, 5)
    num_pow = randint(2, 6)
    my_dict = {1: 'one', 2: 'two'}
    my_func = function(num, num_pow, key='my_dict')
    print(f'{num} ^ {num_pow} = {my_func}')
