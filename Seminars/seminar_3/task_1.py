# Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков


def first_method(lst: list[int]) -> None:
    new_lst = []
    for el in lst:
        if el not in new_lst:
            new_lst.append(el)
    print(*new_lst)


def second_method(lst: list[int]) -> None:
    new_set = set(lst)
    print(*list(new_set))


lst = [1, 2, 3, 5, 2, 5, 7, 1]
first_method(lst)
second_method(lst)
