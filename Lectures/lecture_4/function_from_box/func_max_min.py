"""max(iterable, *[,key, default]) или max(arg1, arg2, *args[, key])"""

# Функция min() работает аналогично

lst_1 = []
lst_2 = [42, 256, 73]
lst_3 = {('Alex', 125_000), ('Jon', 96_000), ('Anton', 55_000)}
print(max(lst_1, default='empty'))
print(max(lst_2))
print(max(lst_3, key=lambda x: x[1]))

