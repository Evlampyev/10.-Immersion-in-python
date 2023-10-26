# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

my_tuple = (1, '2', 3.14, [1, 2], True, '1')
my_dict = {}
for el in my_tuple:
    if type(el) not in my_dict:
        my_dict[type(el)] = [el]
    else:
        my_dict[type(el)] += [el]


print(my_dict)
