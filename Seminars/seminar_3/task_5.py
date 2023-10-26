# Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

from random import randint

lst = [randint(1, 10) for i in range(15)]
print(lst)
lst_odd = []
for i in range(len(lst)):
    if lst[i] % 2 == 1:
        lst_odd.append(i + 1)
print(lst_odd)
