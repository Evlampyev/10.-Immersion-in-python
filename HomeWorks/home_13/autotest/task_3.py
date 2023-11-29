class MyError(Exception):
    pass


class InvalidNameError(MyError):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f'Invalid name: {self.data}. Name should be a non-empty string.'


class InvalidAgeError(MyError):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f'Invalid age: {self.data}. Age should be a positive integer.'


class InvalidIdError(MyError):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return (f'Invalid id: {self.data}. '
                f'Id should be a 6-digit positive integer between 100000 and 999999.')


class TextValidation:
    """Дескриптор проверки текста на правильность"""

    @classmethod
    def validate(cls, value: str):
        if not isinstance(value, str) or not value.istitle() or len(value) == 0:
            raise InvalidNameError(value)

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value: str):
        self.validate(value)
        return setattr(instance, self.name, value)


class Person:
    first_name = TextValidation()
    second_name = TextValidation()
    patronymic = TextValidation()

    def __init__(self, first_name: str, second_name: str, patronymic: str, age: int):
        self.first_name = first_name
        self.second_name = second_name
        self.patronymic = patronymic
        if 18 <= age <= 65:
            self.age = age
        else:
            raise InvalidAgeError(age)

    def get_age(self):
        return self.age

    def birthday(self):
        self.age += 1

    def __str__(self):
        return (f'Имя: {self.second_name} {self.first_name} {self.patronymic}, '
                f'возраст: {self.age}')


class Employee(Person):

    def __init__(self, *args):
        super().__init__(args[0], args[1], args[2], args[3])
        if 99_999 < args[-1] <= 999_999:
            self.u_id = args[-1]
        else:
            raise InvalidIdError(args[-1])
        self.level_access = self.get_level()

    def get_level(self):
        return sum(list(int(el) for el in str(self.u_id))) % 7

    def __str__(self):
        return (f'Employer: {self.second_name} {self.first_name} {self.patronymic}, '
                f'{self.u_id = }, {self.level_access = }')


if __name__ == '__main__':
    user = Person('Alex', 'Ivanov', 'Petrovich', 23)
    print(user)

    emp = Employee('Alex', 'Ivanov', 'Petrovich', 23, 12345)
    print(emp)
