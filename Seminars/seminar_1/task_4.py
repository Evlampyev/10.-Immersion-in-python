"""Пользователь вводит число от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двузначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25
Если число не из диапазона, запросите новое число. Откажитесь от магических чисел
В коде должны быть один input и один print"""

num = int(input("Введите число от 1 до 999: "))

while num < 1 or num > 999:
    num = int(input("Введите число от 1 до 999: "))

if 1 < num < 10:
    result = num * num
elif 9 < num < 100:
    result = (num // 10) * (num % 10)
else:
    result = (num % 10 * 100) + (num // 10 % 10) * 10 + num // 100
print(result)
