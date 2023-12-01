class MyException(Exception):
    def __init__(self, msg: str = 'Ошибка! '):
        self.msg = msg

    def __str__(self):
        return f'{self.msg}'


class ValueInRangeError(MyException):
    """Вхождение значения в диапазон"""

    def __init__(self, minimum: int, maximum: int):
        self.min = minimum
        self.max = maximum
        self.msg = f'Значение не попало в допустимый диапазон от {self.min} до {self.max}'
        super().__init__(self.msg)


class LevelException(MyException):
    """Исключение уровня доступа"""

    def __init__(self, level: int):
        self.need_level = f'Минимально допустимый уровень для этой организации {level}'
        super().__init__(self.need_level)


class VerificationError(MyException):
    """Исключение доступа пользователя"""

    def __init__(self, name: str):
        self.user_msg = f'Такого пользователя нет в организации {name}'
        super().__init__(self.user_msg)
