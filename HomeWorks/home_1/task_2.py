"""Проверка числа на простоту"""
from math import sqrt

num: int = 4
if num <= 1 or num > 100000:
    print("Число должно быть больше 1 и меньше 100000")
else:
    count: int = 0
    i = 2

    while i <= int(sqrt(num)) and count == 0:
        if num % i == 0:
            count += 1
        i += 1

    if count > 0:
        print(f"{num} является составным числом")
    else:
        print(f"{num} является простым числом")
