"""Запись методом write"""

text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
with open('../new_data.txt', 'a', encoding='utf-8') as f:
    res = f.write(text)
print(f'{res = }\n{len(text) = }')

# Метод не добавляет символ перехода на новую строку. Если произвести несколько
# записей, они “склеиваются” в файле.
print('---------------------------')
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('../new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        # res = f.write(line)  # в этом случае все склеится в одну строку
        res = f.write(f'{line}\n')  # будет осуществлен перенос на новую строку
        print(f'{res = }\n{len(line) = }')

# Метод не добавляет символ перехода на новую строку. Если произвести несколько
# записей, они “склеиваются” в файле.
