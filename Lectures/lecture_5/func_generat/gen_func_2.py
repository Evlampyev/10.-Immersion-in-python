def factorial(n):
    number = 1
    for j in range(1, n + 1):
        number *= j
    yield number


my_iter = iter(factorial(4))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))  # StopIteration
