# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

from string import ascii_lowercase
from pytest import main, fixture

ALLOWED_LETTERS = ascii_lowercase + ' '


def delete_char(text: str) -> str:
    return ''.join(filter(lambda x: x in ALLOWED_LETTERS, text.lower()))


@fixture
def result():
    return 'abc'


def test_1(result):
    assert (delete_char('abc') == result)


def test_2(result):
    assert (delete_char('ABC') == result)


def test_3(result):
    assert (delete_char('a.b.c') == result)


def test_4(result):
    assert (delete_char('abcабв') == result)


def test_5():
    assert (delete_char('Hello, мир!') == 'hello ')


if __name__ == '__main__':
    main()
