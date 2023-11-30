from prime_unittest import is_prime
from unittest import TestCase, main
import io
from unittest.mock import patch


class TestPrime(TestCase):

    def test_is_prime(self):
        self.assertFalse(is_prime(42))  # ожидает получить False
        self.assertTrue(is_prime(73))  # # ожидает получить True

    def test_type(self):
        self.assertRaises(TypeError, is_prime, 3.14)
        # ожидает ошибку типа (аргумент один)
        # если вызвать функцию is_prime (аргумент два) и передать ей
        # число 3.14 (аргумент три)

    def test_value(self):
        with self.assertRaises(ValueError):
            is_prime(-100)
            is_prime(1)
        # Менеджер контекста (with) для утверждения ошибки и внутри контекста
        # дважды запускаем функцию. assertRaises во всех случаях будет
        # ожидать ValueError (ошибку значения)

    @patch('sys.stdout', new_callable=io.StringIO) # декоратор
    def test_warning_false(self, mock_stdout):
        self.assertFalse(is_prime(100_000_001))
        self.assertEqual(mock_stdout.getvalue(),
                         'If the number P is prime, the check may take a long '
                         'time.\nWorking...\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_warning_true(self, mock_stdout):
        self.assertTrue(is_prime(100_000_007))
        self.assertEqual(mock_stdout.getvalue(),
                         'If the number P is prime, the check may take a long '
                         'time.\nWorking...\n')

    if __name__ == '__main__':
        main()
