"""Шаблон для замыкания"""


# def one(a):
#     def two(b):
#
#         ...
#         return result
#     return two
#
#
# closure = one(data)


def func(a):
    x = 42
    res = x + a
    return res


x = 73 # переменная никак не влияет на вычисления в функции
print(func(64))
