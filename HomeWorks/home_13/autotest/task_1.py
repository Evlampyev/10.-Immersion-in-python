from functools import total_ordering


class MyException(Exception):
    pass


class NegativeValueError(MyException):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        if self.name == '_width':
            return f'Ширина должна быть положительной, а не {self.value}'
        else:
            return f'Высота должна быть положительной, а не {self.value}'


class NotNegativeValue:
    # @classmethod
    def validate(self, value: float):
        if value <= 0:
            raise NegativeValueError(self.name, value)

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.name, value)


@total_ordering
class Rectangle:
    width = NotNegativeValue()
    height = NotNegativeValue()

    def __init__(self, width: float, height: float = None):
        self.width = width
        self.height = height if height is not None else width

    def perimeter(self):
        return (self.width + self.height) * 2

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.width + other.width, self.height + other.height)

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(abs(self.width - other.width),
                             abs(self.height - other.height))

    def __lt__(self, other):
        return self.area() < other.area()

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __str__(self):
        return f'Прямоугольник со сторонами {self.width} и {self.height}'


if __name__ == '__main__':
    rect1 = Rectangle(-5)  # rect2 = Rectangle(3, 7)
    rect1.width = -2
    print(rect1)

    #
    # print(f"Периметр rect1: {rect1.perimeter()}")
    # print(f"Площадь rect2: {rect2.area()}")
    # print(f"rect1 < rect2: {rect1 < rect2}")
    # print(f"rect1 == rect2: {rect1 == rect2}")
    # print(f"rect1 <= rect2: {rect1 <= rect2}")
    #
    # rect3 = rect1 + rect2
    # print(f"Периметр rect3: {rect3.perimeter()}")
    # rect4 = rect1 - rect2
    # print(f"Ширина rect4: {rect4.width}")
