"""Позиционные и ключевые параметры функции"""


def func(position_only, /, positional_or_keyword, *, keyword_only):
    pass


def standart_arg(arg):
    """Пример обычной функции"""
    print(arg)


def pos_only_arg(arg, /):
    """Пример только позиционной функции"""
    print(arg)


def kwd_only_arg(*, arg):
    """Пример только ключевой функции"""
    print(arg)


standart_arg(42)
standart_arg(arg=42)

pos_only_arg(42)
# pos_only_arg(arg=42)  # TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'

# kwd_only_arg(42)  # TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given
kwd_only_arg(arg=42)
