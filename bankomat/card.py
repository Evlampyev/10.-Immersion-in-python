"""Карта"""
from money import Money


class Card:
    """Карта пользователя"""

    def __init__(self, money: Money = Money(0, '₽')):
        self.my_money = money
        self.count_step = 0

    def get_money(self) -> Money:
        """геттер"""
        return self.my_money

    def set_money(self, money) -> None:
        """сеттер"""
        self.my_money = money

    def chech_money_on_card(self, money) -> bool:
        return self.my_money >= money

    def __add__(self, other):
        self.my_money += other

    def __sub__(self, other):
        self.my_money -= other
