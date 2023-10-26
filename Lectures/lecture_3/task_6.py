"""Множества"""

my_set = {1, 2, 3, 4, 5, 6, 7}
print(my_set)

my_f_set = frozenset((1, 2, 3, 4, 5, 6, 7))
print(type(my_f_set))
print(my_f_set)

my_set.add(10)  # добавление элемента в множество
print(my_set)

# несколько элементов добавлять нельзя!!

my_set.remove(6)
print(f"удалили 6 {my_set}")  # при удалении (методом remove) не существующего элемента будет ошибка
my_set.remove(10)  # Ошибка будет
my_set.discard(10)  # Ошибки не будет, даже если этого элемента нет в множестве
