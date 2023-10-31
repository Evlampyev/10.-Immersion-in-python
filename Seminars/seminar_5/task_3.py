# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

# task_2
my_str = 'Самостоятельно сохраните в переменной строку текста'
my_dict = {char: ord(char) for char in my_str}
print(my_dict)

# task_3
iter_for_my_dict = iter(my_dict.items())
print(next(iter_for_my_dict))
print(next(iter_for_my_dict))
print(next(iter_for_my_dict))
print(next(iter_for_my_dict))
print(next(iter_for_my_dict))
