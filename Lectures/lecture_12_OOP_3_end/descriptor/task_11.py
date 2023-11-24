class Range:
    """Класс-дескриптор Range"""

    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        """Контроль имён"""
        # Метод срабатывает при определении имён свойств. В нашем случае это переменных
        # уровня класса, определённые сразу после заголовка класса Student.
        # Обратите внимание на локальную переменную param_name, которая получает имя
        # создаваемой переменной с символом подчёркивания в начале.
        # Дандер занимается инкапсуляцией за нас, т.е. прячет age в _age и т.д.
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        """Контроль получения значений"""
        # Функция getattr() используется для получения у объекта instance значения
        # для свойства self.param_name, того самого с подчёркиванием в начале.
        # Мы ничего не меняем, а лишь возвращаем значение свойства экземпляра
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        """Контроль присвоение значений"""
        self.validate(value)  # проверка валидации значения
        setattr(instance, self.param_name, value)
        # присваивает у экземпляра instance параметру self.param_name значение value

    def __delete__(self, instance):
        """Контроль удаления атрибутов"""
        # Делейтор, запрещает удаление
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, int):  # если значение не является целым числом,
            raise TypeError(
                f'Значение {value} должно быть целым числом')  # вызываем TypeError
        if self.min_value is not None and value < self.min_value:
            raise ValueError(
                f'Значение {value} должно быть больше или равно {self.min_value}')
        if self.max_value is not None and value >= self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше {self.max_value}')
        # В случае прохождения всех проверок метод ничего не возвращает.
        # Он позволяет выполняться коду дальше


class Student:
    """Класс для хранения информации о студентах"""
    age = Range(3, 103)
    grade = Range(1, 11 + 1)
    office = Range(3, 42 + 1)

    def __init__(self, name, age, grade, office):
        self.name = name
        self.age = age
        self.grade = grade
        self.office = office

    def __repr__(self):
        return f'Student(name={self.name}, age={self.age}, grade={self.grade}, office={self.office})'


if __name__ == '__main__':
    std_one = Student('Архимед', 12, 4, 29)
    std_other = Student('Аристотель', 2406, 5, 17)
    # ValueError: Значение 2406 должно быть меньше 103
    print(f'{std_one = }')
    std_one.age = 15
    print(f'{std_one = }')
    std_one.grade = 11.0  # TypeError: Значение 11.0 должно быть целым числом
    std_one.office = 73  # ValueError: Значение 73 должно быть меньше 42
    del std_one.age  # AttributeError: Свойство "_age" нельзя  удалять
    print(f'{std_one.__dict__ = }')
