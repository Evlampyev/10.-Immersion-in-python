# Создайте класс с базовым исключением и дочерние классы исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class LevelException(Exception):
    def __init__(self, needed_level):
        self.needed_level = needed_level

    def __str__(self):
        return f'Минимально необходимый уровень доступа: {self.needed_level}'


class AccessException(LevelException):
    def __init__(self, not_need_level):
        super().__init__(not_need_level)

    def __str__(self):
        return f'У вас нехватает уровня доступа, ваш уровень {self.needed_level}'


if __name__ == '__main__':
    # raise LevelException(1)
    raise AccessException(2)
