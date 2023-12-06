from functools import total_ordering


class MultiplicityMoney:
    """Дескриптор. Проверка на кратность денежных сумм"""

    def __init__(self, multiple: int):
        self.multiple = multiple

    def validate(self, value):
        return value % self.multiple == 0

    def __set_name__(self, owner, name):
        self.name = '_' + name
        return self.name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validate(value):
            return setattr(instance, self.name, value)
        else:
            raise ValueError("Сумма должна быть кратной 50: ")


@total_ordering
class Money:
    # money = MultiplicityMoney(50)

    def __init__(self, money: float, currency: str):
        """
        Инициализация денежной единицы
        :param money: int
        :param currency: str
        """
        self.money = money
        self.currency = currency

    def __str__(self) -> str:
        return f"{self.money}{self.currency}"

    def __lt__(self, other):
        return self.money < other.money and self.currency == other.currency

    def __eq__(self, other):
        return self.money == other.money and self.currency == other.currency

    def __add__(self, other):
        return Money(self.money + other.money, self.currency)

    def __sub__(self, other):
        return Money(self.money - other.money, self.currency)

    def __mul__(self, other):
        if isinstance(other, int | float):
            return Money(round(self.money * other), self.currency)
        else:
            raise TypeError("Не верный тип данных")

    def __iadd__(self, other):
        self.money = self.money + other.money
        return self

    def __isub__(self, other):
        self.money = self.money - other.money
        return self

    def __imul__(self, other: float | int):
        if isinstance(other, float | int):
            self.money = round(self.money * other)
            return self
        else:
            raise TypeError("Не верный тип данных")
