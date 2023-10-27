# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.


letters = 'Alex'
words = 'asd dsf'
text = '13'
s = 'letter s'

# ТАК ЛУЧШЕ НИКОГДА НЕ ДЕЛАТЬ! НЕ МЕНЯТЬ НАЗВАНИЯ ПЕРЕМЕННЫХ
def change_name():
    new_dict = {}
    for key, value in globals().items():
        if key.endswith('s') and len(key) != 1:
            new_dict[key[:-1]] = value
            new_dict[key] = None
    globals().update(new_dict)


print(globals())
change_name()

print(letter)
print(word)
print(globals())
