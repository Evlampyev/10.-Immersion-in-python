"""Список"""
import copy

lst_1 = list()  # пустой список
lst_2 = []  # пустой список

lst_3 = [3.14, 'pi', 123]

print(lst_1, lst_2, lst_3, sep='\n')

lst_3.append("777")
print(*lst_3)

lst_2.append(1)
lst_2.append(2)
lst_2.append(3)

lst_3.extend(lst_2)  # добавления списка в список, но не списком,
# а# как элементы
print(lst_3)

lst_3.pop()  # удаление последнего элемента списка, очень быстро
print(lst_3)
lst_3.pop(1)  # удаление элемента с индексом 1
print(lst_3)

print(lst_3.index(3))  # ищет первое вхождение, но можно менять диапазон
print(lst_3.index(3, 2,10))  # ищет первое вхождение, начиная с 2 по 10


# метод copy() - поверхостное копирование, то есть верхний уровень
# Если матрица, то для её копирования нужно использовать copy.deepcopy()