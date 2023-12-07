# from unittest import TestCase, main
from functools import total_ordering


class MyException(Exception):
    def __init__(self, msg: str = ''):
        self.msg = msg

    def __str__(self):
        return self.msg


class NegativeValueError(MyException):
    def __init__(self, msg=''):
        self.msg = msg
        super().__init__(self.msg)


@total_ordering
class Rectangle:

    @staticmethod
    def check_value(value):
        if not isinstance(value, (float, int)):
            raise TypeError("Не верный тип данных")
        if value <= 0:
            raise NegativeValueError()

    def __init__(self, width: float | int, height: float | int = None):
        self.check_value(width)
        self._width = width
        if height is None:
            self._height = width
        else:
            self.check_value(height)
            self._height = height

    def get_area(self):
        return self._width * self._height

    def get_perimetr(self):
        return self._width * 2 + self._height * 2

    def __add__(self, other: 'Rectangle'):
        if isinstance(other, Rectangle):
            new_width = self._width + other._width
            perimeter = self.get_perimetr() + other.get_perimetr()
            new_height = perimeter / 2 - new_width
            return Rectangle(new_width, new_height)

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            if self.get_perimetr() < other.get_perimetr():
                self, other = other, self
            new_width = abs(self._width - other._width)
            perimetr = self.get_perimetr() - other.get_perimetr()
            new_height = perimetr / 2 - new_width
            return Rectangle(new_width, new_height)

        else:
            raise TypeError("Другой объект не прямоугольник")

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if isinstance(value, (int | float)):
            self.check_value(value)
            self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if isinstance(value, (int | float)):
            self.check_value(value)
            self._height = value

    def __str__(self):
        return f'Прямоугольник со сторонами {self._width} и {self._height}'

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


# class MyTest(TestCase):
#
#     def setUp(self):
#         self.rc_1 = Rectangle(3, 4)
#
#     def test_width(self):
#         self.assertEqual(Rectangle(5).width, 5)
#
#     def test_height(self):
#         self.assertEqual(Rectangle(3, 4).height, 4)
#
#     def test_perimetr(self):
#         self.assertEqual(Rectangle(5).get_perimetr(), 20)
#
#     def test_area(self):
#         self.assertEqual(Rectangle(3, 4).get_area(), 12)
#
#     def test_addition(self):
#         self.assertEqual(Rectangle(5) + self.rc_1, Rectangle(8, 6))


if __name__ == '__main__':
    # main()
    r1 = Rectangle(3, 4)
    r2 = Rectangle(5)
    print(r1 + r2)
