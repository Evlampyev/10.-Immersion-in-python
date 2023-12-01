# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

# Напишите для задачи 1 тесты doctest.
# Проверьте следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

from string import ascii_lowercase
from doctest import testmod

ALLOWED_LETTERS = ascii_lowercase + ' '


def delete_char(text: str) -> str:
    """
    Удаление всех символов кроме латинских маленьких и пробелов
    :param text: str
    :return: str
    >>> delete_char('abc')
    'abc'
    >>> delete_char('ABC')
    'ABC'
    >>> delete_char('a.b.c')
    'abc'
    >>> delete_char("abcабв")
    'abc'
    >>> delete_char('Hello, мир!')
    'hello '
    """
    return ''.join(filter(lambda x: x in ALLOWED_LETTERS, text.lower()))


if __name__ == '__main__':
    testmod(verbose=True)
