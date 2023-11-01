# Создайте функцию генератор чисел Фибоначчи fibonacci.

def fibonacci():
    first = 0
    second = 1
    count = 1
    while True:
        yield first
        first, second = second, first + second


f = fibonacci()
for i in range(10):
    print(next(f))
