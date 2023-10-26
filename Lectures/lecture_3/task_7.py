"""Логические операции с множествами"""

my_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
other_set = {7, 8, 9, 10, 11, 12}
new_set = my_set & other_set  # пересечение множеств
print(f"{my_set = } \n{other_set = } \n{new_set = }")

new_set = my_set | other_set  # объединение множеств
print(f"{my_set = } \n{other_set = } \n{new_set = }")

new_set = my_set - other_set  # вычитание множеств
print(f"{my_set = } \n{other_set = } \n{new_set = }")

new_set = other_set - my_set  # вычитание множеств
print(f"{my_set = } \n{other_set = } \n{new_set = }")
