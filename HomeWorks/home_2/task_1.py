"""Перевод в шестнадцатеричную СС"""
num: int = 4096
BASE_NUMBER_SYSTEM = 16
hex_list: list[str] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
result: str = ''
temp: int = num
while temp:
    i = temp % BASE_NUMBER_SYSTEM
    temp //= BASE_NUMBER_SYSTEM
    result = hex_list[i] + result
print(f'Шестнадцатеричное представление числа: {result}')
print(f'Проверка результата: {hex(num)}')
