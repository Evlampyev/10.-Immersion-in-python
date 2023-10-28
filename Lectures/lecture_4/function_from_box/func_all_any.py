"""all(iterable) и any(iterable)"""


def all_use(numbers: list[int]) -> None:
    """Итог конъюнкция всех результатов"""
    if all(map(lambda x: x > 0, numbers)):
        print("Все элементы положительные")
    else:
        print('В последовательности есть отрицательные и/или нулевые элементы')


def any_use(numbers: list[int]) -> None:
    """Итог дизъюнкция всех результатов"""
    if any(map(lambda x: x < 0, numbers)):
        print('В последовательности есть отрицательные и/или нулевые элементы')
    else:
        print("Все элементы положительные")


my_numbers = [42, -73, 1024]
all_use(my_numbers)
any_use(my_numbers)
