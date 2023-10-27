# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.

from random import randint


def bubble_sort(my_list: list):
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            if my_list[i] < my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]


print(lst := [randint(10, 100) for _ in range(10)])  # моржовый оператор
# можно сразу присвоить и использовать, как while
bubble_sort(lst)
print(lst)
