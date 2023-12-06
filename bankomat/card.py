"""Карта"""
from bankomat.money import Money
from logging import basicConfig, INFO, getLogger

FORMAT = '[{levelname:<8}] {asctime}: {funcName} -> {msg}'


class Card:
    """Карта пользователя"""
    currency = '₽'

    def __init__(self, money: Money = Money(0, currency)):
        self._my_money = money
        self._count_step = 0
        card_logger.info(
            f'Инициализация карты, баланс карты: {self._my_money}, кол-во операций: {self._count_step}')

    @property
    def my_money(self) -> Money:
        """геттер"""
        card_logger.info(f'Получение баланса карты: {self._my_money}')
        return self._my_money

    @my_money.setter
    def my_money(self, money) -> None:
        """сеттер"""
        card_logger.info(f'Баланс карты: {self._my_money}, был изменен на {money}')
        self._my_money = money
        self._count_step += 1

    def check_money_on_card(self, money) -> bool:
        card_logger.info(
            f'Проверка наличия денежных средств на карте. Баланс {self._my_money}. Запрошено: {money}')
        return self._my_money >= money

    def check_count_operation(self) -> Money:
        interest = Money(0, self.currency)
        if (self._count_step + 1) % 3 == 0:
            interest = Money(self.my_money.money * 0.03, self.currency)
            card_logger.info(
                f'Получение процента на остаток после 3-х операций в размере {interest}')
            self._my_money += interest
        return interest

    def __str__(self):
        return f'Баланс карты: {self.my_money}'


basicConfig(filename=f'log/{__name__}.log', filemode='w', level=INFO,
            encoding='utf-8', format=FORMAT, style='{')
card_logger = getLogger(__name__)
