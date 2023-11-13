"""Функция может принимать другую функцию в качестве параметра"""


def main(func):
    def wrapper(*args, **kwargs):
        ...
        result = func(*args, **kwargs)
        ...
        return result
    return wrapper


def my_func(data):
    ...
    return my_res


deco = main(my_func)
