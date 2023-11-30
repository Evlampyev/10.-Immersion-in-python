from my_error import ValueInRangeError


class NumberCheck:
    def __init__(self, minimum: int, maximum: int):
        self.min = minimum
        self.max = maximum

    def validate_value(self, value: float | int) -> None:
        if not isinstance(value, int | float):
            raise ValueError
        if not 1 <= value <= 7:
            raise ValueInRangeError(self.min, self.max)

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate_value(value)
        return setattr(instance, self.name, value)


class User:
    level_access = NumberCheck(1, 7)

    def __init__(self, name: str, u_id: str, level_access: int):
        self.name = name
        self.u_id = u_id
        self.level_access = level_access

    def __str__(self):
        return f'Уровень доступа: {self.level_access}, Идентификатор: {self.u_id}, Пользователь: {self.name}'

    def __eq__(self, other):
        return self.name == other.name and self.u_id == other.u_id
