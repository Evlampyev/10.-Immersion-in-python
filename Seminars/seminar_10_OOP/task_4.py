# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

from task_3 import User


class Employee(User):
    def __init__(self, employer_id: str, sex: str,
                 surname: str, name: str, patronymic: str = None,
                 age: int = 18, phone: str = None):
        User.__init__(self, sex, surname, name, patronymic, age, phone)
        self.id = employer_id
        self.access_level = self.set_access_level()

    def set_id(self, value) -> None:
        self.id = value

    def get_id(self) -> str:
        return self.id

    def set_access_level(self):
        level = 0
        num = self.id
        return sum(map(int, list(num))) % 7


if __name__ == '__main__':
    emp_1 = Employee('123456', 'men',
                     'Ivanov', 'Petr', 'Alexandrovich',
                     25, '8-922-544')
    print(emp_1)
    print(f'{emp_1.id = }\t{emp_1.access_level = }')

    emp_2 = Employee('12312', 'female',
                 'Ivanova', 'Glasha', 'Alexandrovna',
                 24, '8-922-514')
    print(emp_2)
    print(f'{emp_2.id = }\t{emp_2.access_level = }')
    print(f'{emp_2.get_age() = }')
    emp_2.birthday()
    print(f'{emp_2.get_age() = }')

