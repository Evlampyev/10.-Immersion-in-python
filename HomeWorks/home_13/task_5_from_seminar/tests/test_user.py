from unittest import main, TestCase
from ..user import User


class TestUser(TestCase):

    def test_init_user(self):
        self.assertEquals(f"{User('Name', 1, 2)}",
                          "Уровень доступа: 2, Идентификатор: 1, Пользователь: Name")


if __name__ == '__main__':
    main()
