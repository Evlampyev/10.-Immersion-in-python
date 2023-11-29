from typing import Union


class MyError(Exception):
    pass


class InvalidTextError(MyError):
    def __str__(self):
        return f'Invalid text: . Text should be a non-empty string.'


class InvalidNumberError(MyError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (f'Invalid number: {self.value}. '
                f'Number should be a positive integer or float')


class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        if isinstance(text, str) and text != "":
            self.text = text
        else:
            raise InvalidTextError
        if isinstance(number, int) and number > 0 or isinstance(number, float):
            self.number = number
        else:
            raise InvalidNumberError(number)

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'


if __name__ == '__main__':
    invalid_archive_instance = Archive("", -5)
    print(invalid_archive_instance)
