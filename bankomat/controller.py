from card import Card
from money import Money
from bankomat import Bankomat
from terminal import Terminal as MyInterface


class Controller:
    """Работа всей системы"""
    CHECKING_NUM = 50
    CURRENCY = '$'

    def __init__(self, money=1_000):
        user_card = Card(Money(money, self.CURRENCY))
        bankomat = Bankomat(self.CURRENCY)
        MyInterface.print_text("Здравствуйте")

        while (choice := self.request_to_perform_operations()) != 3:
            match choice:
                case 1:
                    MyInterface.print_text("Внесите ваши деньги: ")
                    money = self.get_right_amount()
                case 2:

                    MyInterface.print_text("Укажите сумму для снятия: ")
                    withdrawable_money = self.get_right_amount()
                    if bankomat.check_pick_up_from_bank(withdrawable_money) and user_card.chech_money_on_card(
                            withdrawable_money):
                        user_card.__sub__(withdrawable_money)
                        bankomat.pick_up_from_bank(withdrawable_money)
                        MyInterface.print_text(
                            f'Выдана сумма: {withdrawable_money}. Баланс карты: {user_card.my_money}')  # Баланс карты почему-то 0

    @staticmethod
    def checking_multiplicity(num) -> bool:
        """
        Проверка на кратность 50
        :param num:
        :return: bool
        """
        return num % Controller.CHECKING_NUM == 0

    @staticmethod
    def request_to_perform_operations() -> int:
        """Запрос на выполнение операций"""
        lst = [
            "   Какую операцию будем выполнять: ",
            "1. Пополнить баланс карты",
            "2. Снять наличные с карты",
            "3. Выйти"]
        for el in lst:
            MyInterface.print_text(el)
        choice = MyInterface.input_data()
        return choice

    def get_right_amount(self) -> Money:
        money = MyInterface.input_data()
        while not self.checking_multiplicity(money):
            MyInterface.print_text("Сумма должна быть кратной 50: ")
            money = MyInterface.input_data()
        return Money(money, self.CURRENCY)
