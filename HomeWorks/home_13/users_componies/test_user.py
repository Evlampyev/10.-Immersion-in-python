from unittest import main, TestCase
from .user import User


class TestUser(TestCase):
    def setUp(self):
        self.user = User('Name', '1', 2)

    def test_init_user(self):
        self.assertEqual(f"{self.user}",
                         "Уровень доступа: 2, Идентификатор: 1, "
                         "Пользователь: Name")

    def test_equal(self):
        self.assertEqual(self.user, User('Name', '1', 5))


if __name__ == '__main__':
    main(verbosity=2)
