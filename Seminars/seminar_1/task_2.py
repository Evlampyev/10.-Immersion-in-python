"""Посчитайте сумму чётных элементов от 1 до n исключая кратные e."""

n, e = map(int, input("Введите  n и e: ").split())

i = 0
result: int = 0

while i <= n:
    if i % e:
        result += i
    i += 2
print(f"Сумма четных от 1 до {n} исключая кратные {e} равна {result}")
