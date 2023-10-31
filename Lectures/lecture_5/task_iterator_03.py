"""next(iterator[, default])"""

data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))  # При завершении элементов выбрасывается исключение StopIteration

data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter, 42))  # Второй параметр функции next нужен для возврата значения по умолчанию
# вместо выброса исключения StopIteration

print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
