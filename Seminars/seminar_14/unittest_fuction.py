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
from unittest import main, TestCase

ALLOWED_LETTERS = ascii_lowercase + ' '


def delete_char(text: str) -> str:
    return ''.join(filter(lambda x: x in ALLOWED_LETTERS, text.lower()))


class MyTEst(TestCase):
    def test_1(self):
        self.assertEquals(delete_char('abc'), 'abc')

    def test_2(self):
        self.assertEquals(delete_char('ABC'), 'abc')

    def test_3(self):
        self.assertEquals(delete_char('a.b.c'), 'abc')

    def test_4(self):
        self.assertEquals(delete_char('abcабв'), 'abc')

    def test_5(self):
        self.assertEquals(delete_char('Hello, мир!'), 'hello ')


if __name__ == '__main__':
    main(verbosity=2)
