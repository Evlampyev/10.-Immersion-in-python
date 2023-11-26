"""Несколько except для одного try"""
#  правильнее использовать несколько отдельных try except

def hundred_div_num(text: str = None) -> tuple[int, float]:
    while True:
        try:
            num = int(input(text))
            div = 100 / num
            break
        except ValueError as e:  # перехват ошибки ввода
            print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
                  f'Попробуйте снова')
        except ZeroDivisionError as e:  # перехват деления на ноль
            div = float('inf')  # бесконечность
            break
    return num, div


if __name__ == '__main__':
    n, d = hundred_div_num('Введите целый делитель: ')
    print(f'Результат операции: "100 / {n} = {d}"')
