with open('../text_data.txt', 'r+', encoding='utf-8') as f:
    print(list(f))
print(f.write('Пока'))  # ValueError: I/O operation on closed file.
# так как файл уже закрыт возникает ошибка
