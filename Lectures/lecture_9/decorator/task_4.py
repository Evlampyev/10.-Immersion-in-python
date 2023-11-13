"""Вложенные декораторы"""
from typing import Callable


def deco_a(func: Callable):
    def wrapper_a(*args, **kwargs):
        print('Старт декоратора A')
        print(f'Запускаю {func.__name__}')
        res = func(*args, **kwargs)
        print(f'Завершение декоратора A')
        return res

    print('Возвращаем декоратор A')
    return wrapper_a


def deco_b(func: Callable):
    def wrapper_b(*args, **kwargs):
        print('Старт декоратора B')
        print(f'Запускаю {func.__name__}')
        res = func(*args, **kwargs)
        print(f'Завершение декоратора B')
        return res

    print('Возвращаем декоратор B')
    return wrapper_b


def deco_c(func: Callable):
    def wrapper_c(*args, **kwargs):
        print('Старт декоратора C')
        print(f'Запускаю {func.__name__}')
        res = func(*args, **kwargs)
        print(f'Завершение декоратора C')
        return res

    print('Возвращаем декоратор C')
    return wrapper_c


@deco_c
@deco_b
@deco_a
def main():
    print('Старт основной функции')


main()

# При запуске кода процесс декорирования начинает снизу вверх, с A, далее B и лишь
# потом C. Прежде чем выполнить код основной функции запускается код верхнего
# декоратора С, далее B, в конце нижний A и только потом код функции main.
# После того как декорированная функция завершила работу и вернула результат декораторы
# завершают работу в обратном старту порядке, снизу вверх. В зависимости от решаемых
# задач порядок декорирования может привести к разным результатам.
