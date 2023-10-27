"""Лямбда функция"""

my_dict = {'two': 2, 'one': 1, 'four': 4, 'ten': 10}
print(f'{my_dict = }')
s_key = sorted(my_dict.items())
s_value = sorted(my_dict.items(), key=lambda x: x[1])  # ключ в 'нулевой' ячейке, а значение в '1'
print(f'{s_key = }\n{s_value = }')
