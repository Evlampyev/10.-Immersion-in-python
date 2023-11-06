"""Запись методом writelines"""

text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('../new_data.txt', 'a', encoding='utf-8') as f:
    f.writelines('\n'.join(text))

# каждая строка запиисана с новой строки, в конце переноса на новую строку нет.
