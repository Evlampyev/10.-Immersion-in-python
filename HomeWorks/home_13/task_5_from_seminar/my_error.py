class MyException(Exception):
    def __init__(self, msg: str):
        self.msg = 'Ошибка! '

    def __str__(self):
        return f'{self.msg}'


class ValueInRangeError(MyException):
    """Вхождение значения в диапазон"""
    def __init__(self, minimum: int, maximum: int):
        self.min = minimum
        self.max = maximum
        self.msg = f'Значение не попало в допустимый диапазон от {self.min} до {self.max}'



