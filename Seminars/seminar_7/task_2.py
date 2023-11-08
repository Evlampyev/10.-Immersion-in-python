# ✔Напишите функцию, которая генерирует псевдоимена.
# ✔Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
# среди которых обязательно должны быть гласные.
# ✔Полученные имена сохраните в файл.

from random import randint, choice

VOWELS = list('уеыаоэёяию')
CONSONANT = list(set([chr(i) for i in range(1072, 1104)]).difference(VOWELS))


def generate_name(file_name: str, count: int = 10) -> None:
    list_name = []
    for _ in range(count):
        name = ''
        for i in range(randint(4, 7)):
            name += choice(VOWELS) if i % 2 == 0 else choice(
                CONSONANT)
        list_name.append(name.title())
        result = '\n'.join(list_name)
    with open(file_name, 'w', encoding='UTF-8') as file:
        file.write(result)


generate_name('names.txt')
