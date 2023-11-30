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
    >>> is_prime(3.14)
    Traceback (most recent call last):
    ...
    TypeError: The number P must be an integer type
    >>> is_prime(-100)
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
    >>> is_prime(1)
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
    >>> is_prime(100_000_001)
    If the number P is prime, the check may take a long time.
    Working...
    False
    >>> is_prime(100_000_007)
    If the number P is prime, the check may take a long time.
    Working...
    True
    """
    if isinstance(num, float):
        raise TypeError('The number P must be an integer type')
    if num <= 1:
        raise ValueError('The number P must be greater than 1')
    if num > 100_000_000:
        print('If the number P is prime, the check may take a long time.\nWorking...')
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    from doctest import testmod

    # testmod() # запуск тестов без вывода на экран
    testmod(verbose=True)  # запуск docтестов с выводом на экран
    # help(is_prime)
