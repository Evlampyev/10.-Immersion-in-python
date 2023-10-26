"""Задача"""
# ✔Напишите программу, которая получает целое число и возвращает его двоичное,
# восьмеричное строковое представление.
# ✔Функции bin и oct используйте для проверки своего результата, а не для решения.
# Дополнительно:
# ✔Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# ✔Избегайте магических чисел
# ✔Добавьте аннотацию типов, где это возможно

num: int = 16
number_systems: list = [2, 7, 8]
result: str = ''
temp: int = num
for i in range(len(number_systems)):
    while temp > 0:
        result = str(temp % number_systems[i]) + result
        temp //= number_systems[i]
    print(f"Система счисления {number_systems[i]} = {result}")
    result: str = ""
    temp = num
