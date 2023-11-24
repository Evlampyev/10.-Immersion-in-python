# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль
# недопустимых значений (отрицательных).
# Используйте декораторы свойств


# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.

from functools import total_ordering


# чтобы уйти от прописывания всех 6 функций сравнения


@total_ordering
class Rectangle:

    @staticmethod
    def check_value(value):
        if not isinstance(value, (float, int)):
            raise TypeError("Не верный тип данных")
        if value <= 0:
            raise ValueError("Не верное значение размера")

    def __init__(self, width: float | int, length: float | int = None):
        self.check_value(width)
        self._width = width
        self.check_value(width)
        self._length = width if length is None else length

    def get_area(self):
        return self._width * self._length

    def get_perimetr(self):
        return self._width * 2 + self._length * 2

    def __add__(self, other: 'Rectangle'):
        if isinstance(other, Rectangle):
            new_length = self._width + other._width
            new_width = self._length + other._length
            return Rectangle(new_length, new_width)

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            if self.get_area() > other.get_area():
                new_length = abs(self._width - other._width)
                new_width = abs(self._length - other._length)
                return Rectangle(new_length, new_width)
            else:
                raise ValueError("Вычитаемое больше уменьшаемого")
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
    def length(self):
        return self._width

    @length.setter
    def length(self, value):
        if isinstance(value, (int | float)):
            self.check_value(value)
            self._width = value

    def __str__(self):
        return f'Прямоугольник со сторонами {self._width} и {self._length}'

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

    # c = Rectangle(-2,4)
