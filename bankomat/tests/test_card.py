from unittest import main, TestCase
from bankomat.money import Money
from bankomat.card import Card


class TestCard(TestCase):
    def setUp(self):
        self.money = Money(100, '₽')
        self.card = Card(self.money)

    def test_balance(self):
        self.assertEqual(f'{self.card}', 'Баланс карты: 100₽')

    def test_get_money(self):
        self.assertEqual(self.card.my_money, Money(100, '₽'))

    def test_set_money(self):
        self.card.my_money = Money(200, '₽')
        self.assertEqual(self.card.my_money.money, 200)

    def test_count_add(self):
        self.card.my_money = Money(200, '₽')
        self.assertEqual(self.card._count_step, 1)

    def test_check_count_operation(self):
        self.card._count_step = 2
        self.assertEqual(self.card.check_count_operation(), Money(3, '₽'))


if __name__ == '__main__':
    main()
