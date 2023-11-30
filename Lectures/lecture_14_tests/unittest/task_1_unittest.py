from unittest import main, TestCase


class TestCaseName(TestCase):
    def test_method(self):
        self.assertEqual(2 * 2, 5, msg='Видимо в этой вселенной не работает')


if __name__ == '__main__':
    main(verbosity=2)  # по умолчанию 1, если 2 - больше информации выводится

