class AccessException(Exception):
    def __init__(self, msg: str = ''):
        self.msg = msg

    def __str__(self):
        return 'Ошибка доступа! ' + self.msg


class LevelException(AccessException):
    def __init__(self, msg: int):
        self.needed_level = f'Минимально необходимый уровень доступа: {msg}'
        super().__init__(self.needed_level)


raise LevelException(1)
