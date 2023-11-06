"""Чтением методом for"""

SIZE = 100
with open('../text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line[:-1])
        print(line.replace('\n', ''))

# Символ переноса строки сохранился в конце каждой строки.
# Если вам необходимо обработать строку без переносов, можно использовать
# срезы line[:-1] или метод замены line.replace('\n', '')
