# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год, full_name для
# вывода полного ФИО и т.п. на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность
# получить текущий возраст.

class User:
    def __init__(self, sex: str, surname: str, name: str, patronymic: str = None,
                 age: int = 18, phone: str = None):
        self.sex = sex
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.__age = age
        self._phone = phone

    def birthday(self):
        self.__age += 1

    def get_age(self):
        return self.__age

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'


if __name__ == '__main__':
    men = User('men', 'Ivanov', 'Petr', 'Igorevich')
    print(men)
    print(f'{men.get_age() = }')
    men.birthday()
    print(f'{men.get_age() = }')


