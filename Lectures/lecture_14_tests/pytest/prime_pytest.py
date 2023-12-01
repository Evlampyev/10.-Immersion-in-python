from math import sqrt


def is_prime(num: int) -> bool:

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
