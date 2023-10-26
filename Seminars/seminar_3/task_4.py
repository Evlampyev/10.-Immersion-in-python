# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.

from random import randint

lst: list = [randint(1, 10) for i in range(15)]
print(lst)
i: int = 0
while i < len(lst):
    if lst.count(lst[i]) == 2:
        el = lst[i]
        lst.remove(el)
        lst.remove(el)
    else:
        i += 1
print(lst)

