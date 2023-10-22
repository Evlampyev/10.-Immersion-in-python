"""Карта"""
from money import Money


class Card:
    """Карта пользователя"""

    def __init__(self, money: Money):
        self.my_money = money

    def get_money(self) -> Money:
        """геттер"""
        return self.my_money

    def set_money(self, money) -> None:
        """сеттер"""
        self.my_money = money

    def __add__(self, other: Money):
        self.my_money.money += other.money

    def __sub__(self, other):
        self.my_money.money -= other.money
