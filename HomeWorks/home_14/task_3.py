import doctest
from decimal import Decimal


class Person:

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        """
        >>> print(Person('Ivanov', 'Ivan', 'Ivanovich', 30).full_name())
        Ivanov Ivan Ivanovich

        :return:
        """
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        """
        >>> per = Person('Ivanov', 'Ivan', 'Ivanovich', 30)
        >>> per.birthday()
        >>> print(per.get_age())
        31
        """
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int,
                 position: str, salary: float):
        """
        >>> emp = Employee("ivanov", "ivan", "ivanovich", 30, "manager", 50000)
        >>> print(emp.last_name)
        Ivanov
        >>> print(emp.salary)
        50000.0

        :param last_name:
        :param first_name:
        :param patronymic:
        :param age:
        :param position:
        :param salary:
        """
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = round(Decimal(salary), 1)

    def raise_salary(self, percent: float):
        """
        >>> emp = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
        >>> emp.raise_salary(10)
        >>> print(emp.salary)
        55000.0

        :param percent:
        :return:
        """
        self.salary = round(self.salary * Decimal(1 + percent / 100), 1)

    def __str__(self):
        """
        >>> emp = Employee("Ivanov","Ivan", "Ivanovich", 30, "manager", 50000)
        >>> print(emp)
        Ivanov Ivan Ivanovich (Manager)

        :return:
        """
        return f'{self.full_name()} ({self.position})'


if __name__ == '__main__':

    # doctest.testmod()

    pr = Employee('Ivanov', 'Ivan', 'Ivanovich', 30, 'man', 1000)
    print(pr)
    print(pr.salary)
    pr.raise_salary(10)
    print(pr.salary)
