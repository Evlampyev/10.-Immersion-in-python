from HomeWorks.home_13.users_componies import Company
from unittest import TestCase, main


class TestCompony(TestCase):
    def setUp(self):
        self.compony = Company('AlexCo', 3)

    def test_get_level(self):
        self.assertEquals(self.compony.access_level, 3)


if __name__ == '__main__':
    main(verbosity=2)
