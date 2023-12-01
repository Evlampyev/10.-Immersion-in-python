# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

from string import ascii_lowercase

ALLOWED_LETTERS = ascii_lowercase + ' '


def delete_char(text: str) -> str:
    return ''.join(filter(lambda x: x in ALLOWED_LETTERS, text.lower()))


if __name__ == '__main__':
    print(delete_char('abc абв b>6'))
