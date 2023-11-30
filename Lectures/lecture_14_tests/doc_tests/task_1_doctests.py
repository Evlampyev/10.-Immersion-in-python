from math import sqrt


def is_prime(num: int) -> bool:
    """
    Проверка числа на простоту
    :param num:
    :return: bol
    >>> is_prime(42)
    False
    >>> is_prime(73)
    True
    """
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    from doctest import testmod

    # testmod() # запуск тестов без вывода на экран
    testmod(verbose=True)  # запуск docтестов с выводом на экран
    # help(is_prime)
