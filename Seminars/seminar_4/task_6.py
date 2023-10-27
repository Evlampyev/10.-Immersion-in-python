# Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.
from random import randint


def find_amount(lst: list, id_1: int, id_2: int) -> float:
    id_1, id_2 = sorted([id_1, id_2])
    if id_1 <= 0:
        id_1 = 0
    # if id_2 >= len(lst):  срезы работают и при выходе за пределы списка
    #     id_2 = len(lst) - 1
    return sum(lst[id_1: id_2 + 1])


print(my_list := [randint(1, 10) for i in range(10)])
print(find_amount(my_list, 8, 10))
