f = open('../text_data.txt', encoding='utf-8')
print(f)
print(list(f))

f.close() # закрытие файла гарантирует сохранение данные в файле
