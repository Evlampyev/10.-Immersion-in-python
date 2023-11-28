# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

from typing import Any


def get_item_from_key(my_dict: dict, key: Any, default: Any = None):
    try:
        return my_dict[key]
    except KeyError:
        return default


if __name__ == '__main__':
    new_dict = {1: 'a', '2': (1, 2, 3)}
    print(get_item_from_key(new_dict, 1, 0))
    print(get_item_from_key(new_dict, 3, 0))
