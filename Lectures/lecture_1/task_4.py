"""Использование в цикле continue"""
num: float = float(input("Введите число: "))
STEP = 2
limit = num - STEP
count: int = - STEP
while count < limit:
    count += STEP
    if count % 12 == 0:
        continue # при вводе числа 20 в выводе не будет числа 12
    print(count)
