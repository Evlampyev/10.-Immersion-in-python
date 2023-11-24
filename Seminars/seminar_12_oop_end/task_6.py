# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.


from functools import \
    total_ordering  # чтобы уйти от прописывания всех 6 функций сравнения


class Value:
    @classmethod
    def check_value(cls, value):
        """Метод валидации значений класса"""
        if not isinstance(value, (float, int)):
            raise TypeError("Не верный тип данных")
        if value <= 0:
            raise ValueError("Значение должно быть больше 0")

    def __set_name__(self, owner, name):  # owner - экземпляр класса
        """Инкапсуляция имен"""
        self.name = '_' + name

    def __get__(self, instance, owner):
        """Получение (геттер) значения instance(экземпляра) по имени"""
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        """Установка(сеттер) значения value, для параметра name, с валидацией """
        self.check_value(value)
        setattr(instance, self.name, value)


@total_ordering
class Rectangle:

    width = Value()
    length = Value()

    # __slots__ = ('width', 'length')

    def __init__(self, width: float | int, length: float | int = None):
        self.width = width
        self.length = width if length is None else length

    def get_area(self):
        return self.width * self.length

    def get_perimetr(self):
        return self.width * 2 + self.length * 2

    def __add__(self, other: 'Rectangle'):
        if isinstance(other, Rectangle):
            new_length = self.width + other.width
            new_width = self.length + other.length
            return Rectangle(new_length, new_width)

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            if self.get_area() > other.get_area():
                new_length = abs(self.width - other.width)
                new_width = abs(self.length - other.length)
                return Rectangle(new_length, new_width)
            else:
                raise ValueError("Вычитаемое больше уменьшаемого")
        else:
            raise TypeError("Другой объект не прямоугольник")

    def __str__(self):
        return f'Прямоугольник со сторонами {self.width} и {self.length}'

    @staticmethod
    def check_rectangle(other):
        if not isinstance(other, Rectangle):
            raise TypeError("Второй объект не прямоугольник")

    def __eq__(self, other):
        self.check_rectangle(other)
        return self.get_area() == other.get_area()

    def __lt__(self, other):
        self.check_rectangle(other)
        return self.get_area() < other.get_area()


if __name__ == '__main__':
    a = Rectangle(4, 6)
    b = Rectangle(2)
    print(a)
    c = a + b
    print(f'c=a+b = {c}')
    d = c - a
    print(f'd=a-b = {d}')

    print(a > b)
    print(a < b)
    print(a != b)
    print(a == b)
    print(a >= b)
    print(a <= b)

    e = Rectangle(2, 4)
    e.width = 6
    print('*' * 8)
    print(e)
    c.length = 'sdf'
