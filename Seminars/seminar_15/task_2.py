from functools import wraps
import sys
from typing import Callable
from logging import basicConfig, NOTSET, getLogger, StreamHandler


def log(func: Callable) -> Callable:
    logger = getLogger(func.__name__)
    logger.addHandler(StreamHandler(sys.stdout))

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        result = func(*args, **kwargs)
        logger.info(f'{args=}, {kwargs=}, {result=}')

    return wrapper


@log
def add_numbers(*args, **kwargs):
    return sum(args)


if __name__ == '__main__':

    basicConfig(filename='log/log_2.log',
                level=NOTSET,
                # datefmt='%H:%M:%S',
                format='[{levelname:<8}] {asctime}: {funcName} -> {msg}',
                style='{')
    add_numbers(1, 2, 10, 15, a=1, b=2, c=3)
