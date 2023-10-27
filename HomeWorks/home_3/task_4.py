# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

lst = [1, 1, 2, 2, 3, 3]
new_lst = list()
my_set = set()
for el in lst:
    if lst.count(el) > 1:
        my_set.add(el)
print(list(my_set))
