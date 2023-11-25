"""Карта"""
from money import Money


class Card:
    """Карта пользователя"""

    def __init__(self, money: Money = Money(0, '₽')):
        self._my_money = money
        self.count_step = 0

    @property
    def my_money(self) -> Money:
        """геттер"""
        return self._my_money

    @my_money.setter
    def my_money(self, money) -> None:
        """сеттер"""
        self._my_money = money
        self.count_step += 1

    def check_money_on_card(self, money) -> bool:
        return self._my_money >= money

    def check_count_operation(self) -> int:
        interest = 0
        if (self.count_step + 1) % 3 == 0:
            interest = self.my_money * 0.03
            self._my_money += interest
        return interest

    def __str__(self):
        return f'Баланс карты: {self.my_money}'
