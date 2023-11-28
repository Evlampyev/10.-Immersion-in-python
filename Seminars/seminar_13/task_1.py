# Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор,
# пока он не введёт целое или вещественное число.
# Обрабатывайте не числовые данные как исключения.

def input_number() -> float | int:
    while True:
        try:
            num = input("Введите число: ")
            return int(num) if num.isdigit() else float(num)
        except ValueError as e:
            print(f'Ошибка: {e}\nПовторите ввод числа: ')


if __name__ == '__main__':
    num = input_number()
    print(f'Введенное число: {num}')
