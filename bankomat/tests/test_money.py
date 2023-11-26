from unittest import TestCase, main
from bankomat.money import Money


class TestMoney(TestCase):

    def setUp(self):
        self.first = Money(100, '$')
        self.second = Money(60, '$')

    def test_add(self):
        self.assertEqual(self.first + self.second, Money(160, '$'),
                         "Сумма считается не верно")

    def test_iadd(self):
        temp = Money(10, '$')
        temp += self.second
        self.assertEqual(temp, Money(70, '$'),
                         "Сумма на месте считается не верно")

    def test_sub(self):
        self.assertEqual(self.first - self.second, Money(40, '$'),
                         "Вычитание считается не верно")

    def test_isub(self):
        temp = Money(150, '$')
        temp -= self.first
        self.assertEqual(temp, Money(50, '$'),
                         'Вычитание на месте работает не работает')

    def test_mul(self):
        self.assertEqual(self.first * 1.5, Money(150, '$'),
                         "Умножение работает не верно")

    def test_imul(self):
        temp = Money(10, '$')
        temp *= 2.5
        self.assertEqual(temp, Money(25, '$'),
                         "Умножение на месте не работает")


if __name__ == '__main__':
    main()
