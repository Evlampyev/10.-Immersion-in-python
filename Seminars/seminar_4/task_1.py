# Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.


def print_text(text: str) -> None:
    words = []
    word = ''
    for ch in text:
        if ch.isalpha():
            word += ch
        else:
            words.append(word.lower())
            word = ''
    words = ' '.join(words).split()
    words.sort()
    max_len = len(max(words, key=len))
    for i, word in enumerate(words):
        print(f'{i+1:>3} {word: >{max_len}}')


data = 'Напишите функцию, которая принимает строку текста.'
print_text(data)
