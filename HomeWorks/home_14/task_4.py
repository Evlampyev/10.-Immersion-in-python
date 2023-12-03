from unittest import main, TestCase
from decimal import Decimal


class Person:

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int,
                 position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        self.salary = round(self.salary * Decimal(1 + percent / 100), 1)

    def __str__(self):
        return f'{self.full_name()} ({self.position})'


class TestEmployee(TestCase):
    def setUp(self):
        self.employee = Employee(
            'ivanov', 'ivan', 'ivanovich', 30,
            'manager', 50000)

    def test_employee_full_name(self):
        self.assertEqual(self.employee.full_name(), 'Ivanov Ivan Ivanovich')

    def test_employee_birthday(self):
        self.employee.birthday()
        self.assertEqual(self.employee.get_age(), 31)

    def test_employee_raise_salary(self):
        self.employee.raise_salary(10)
        self.assertEqual(self.employee.salary, 55000)

    def test_employee_str(self):
        self.assertEqual(f'{self.employee}', 'Ivanov Ivan Ivanovich (Manager)')

    def test_employee_last_name_title(self):
        self.assertFalse(self.employee.last_name == 'Ivan')


if __name__ == '__main__':
    main()
