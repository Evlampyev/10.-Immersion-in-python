from card import Card
from money import Money
from bankomat import Bankomat
from terminal import Terminal as MyInterface


class Controller:
    """Работа всей системы"""

    CURRENCY = '$'
    PERCENT = 0.015
    MULTIPLE = 50

    def __init__(self, money=1_000):
        user_card = Card(Money(money, self.CURRENCY))
        bankomat = Bankomat(self.CURRENCY)
        MyInterface.print_text("Здравствуйте")

        while (choice := self.request_to_perform_operations()) != 4:
            match choice:
                case 1:  # Пополнение баланса карты
                    MyInterface.print_text("Внесите ваши деньги: ")
                    money = self.get_right_amount()
                    interest = Money(0, self.CURRENCY)
                    if money > Money(0, self.CURRENCY):
                        interest = Money(user_card.check_count_operation(), self.CURRENCY)

                        user_card.my_money += money
                        bankomat.put_in_bank(money)
                    MyInterface.print_text(
                        f'|Баланс пополнен на сумму: {money}. {user_card}.\n'
                        f'|Проценты по вкладу: {interest} {bankomat}')

                case 2:  # Снятие наличных с карты
                    interest = Money(0, self.CURRENCY)
                    MyInterface.print_text("Укажите сумму для снятия: ")
                    withdrawable_money = self.get_right_amount()
                    if withdrawable_money > Money(0, self.CURRENCY):
                        commission = self.commission_calculation(withdrawable_money)
                    else:
                        commission = 0
                    withdrawable_money += commission
                    if bankomat.check_pick_up_from_bank(withdrawable_money - commission):
                        if user_card.check_money_on_card(withdrawable_money):
                            user_card.my_money -= withdrawable_money
                            interest = Money(user_card.check_count_operation(),
                                             self.CURRENCY)
                            bankomat.pick_up_from_bank(withdrawable_money - commission)
                            MyInterface.print_text(
                                f'|Выдана сумма: {withdrawable_money - commission}. '
                                f'{user_card}.\n'
                                f'|Проценты по вкладу: {interest} {bankomat}')
                        else:
                            MyInterface.print_text('На карте недостаточно средств')
                    else:
                        MyInterface.print_text('В банкомате недостаточно наличности')
                case 3:  # Получение баланса карты
                    MyInterface.print_text(user_card)
                case 4:
                    pass
            # выход

    @staticmethod
    def request_to_perform_operations() -> int:
        """Запрос на выполнение операций"""
        lst = [
            "   Какую операцию будем выполнять: ",
            "1. Пополнить баланс карты",
            "2. Снять наличные с карты",
            "3. Проверить баланс карты",
            "4. Выйти"]
        for el in lst:
            MyInterface.print_text(el)
        choice = MyInterface.input_data()
        return choice

    def get_right_amount(self) -> Money:
        """Получение верной суммы, кратной 50"""
        while True:
            money = MyInterface.input_data()
            if money % self.MULTIPLE == 0:
                return Money(money, self.CURRENCY)
            else:
                MyInterface.print_text("Сумма должна быть кратной 50: ")

    def commission_calculation(self, money: Money) -> Money:
        """Расчет процентов за снятие денег"""
        commission = self.PERCENT * money.money
        if 0 < commission < 30:
            commission = 30
        elif commission > 600:
            commission = 600
        return Money(commission, self.CURRENCY)
