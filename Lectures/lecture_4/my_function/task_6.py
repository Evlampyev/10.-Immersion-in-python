"""Параметры *args **kwargs"""


#  *args - несколько позиционных аргументов
#  **kwargs - несколько ключевых аргументов
# def func(*args, **kwargs): - принимает любое число позиционных и ключевых аргументов


def school_print(**kwargs):
    for key, value in kwargs.items():
        print(f'по предмету "{key: ^8}" получена оценка {value: >2}')


school_print(химия=5, физика=4, физра=2)
