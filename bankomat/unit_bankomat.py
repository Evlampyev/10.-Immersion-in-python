from money import Money


class Bankomat:

    def __init__(self, currency: str, money=1_000_000):
        """
        Установка банкомата
        :param money: сумма в наличии
        :param currency: валюта
        """
        self.bank_money = Money(money, currency)

    def check_pick_up_from_bank(self, money: Money) -> bool:
        """Проверка на наличие денег в банкомате"""
        if money <= self.bank_money:
            return True
        else:
            return False

    def pick_up_from_bank(self, money: Money):
        """Выдача наличных"""
        self.bank_money -= money

    def put_in_bank(self, money):
        """Пополнить баланс карты"""
        self.bank_money += money

    def quit(self):
        """Выход"""
        pass

    def __str__(self):
        return f"В банкомате {self.bank_money} наличных денег"
