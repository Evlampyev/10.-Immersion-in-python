"""Использование break и else с циклом"""
min_limit: int = 0
max_limit: int = 10
count: int = 3
while count > 0:
    print('Попытка ' + str(count))
    count -= 1
    num = float(input(f'Введи число между {min_limit} и {max_limit}: '))
    if num < min_limit or num > max_limit:
        print('Неверно')
    else:
        break  # прекращение ввода чисел при попадании в диапазон
else:
    print('Исчерпаны все попытки. Сожалею.')
    quit(0)  # выход из программы
print('Было введено число ' + str(num))
