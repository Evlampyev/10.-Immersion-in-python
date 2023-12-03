import pytest


class NegativeValueError(ValueError):
    pass


class Rectangle:
    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(
                    f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height


def test_width():
    rectangle = Rectangle(5)
    assert (rectangle.width == 5)


def test_height():
    rectangle = Rectangle(3, 4)
    assert (rectangle.height == 4)


def test_perimeter():
    rectangle = Rectangle(5)
    assert (rectangle.perimeter() == 20)


def test_area():
    rectangle = Rectangle(3, 4)
    assert (rectangle.area() == 12)


def test_addition():
    rect_1 = Rectangle(5, 3)
    rect_2 = Rectangle(1, 4)
    rect = rect_1 + rect_2
    assert (rect == Rectangle(6, 7))


def test_negative_width():
    try:
        rect = Rectangle(-2)
    except NegativeValueError:
        assert True


def test_negative_height():
    try:
        rect = Rectangle(5, -4)
    except NegativeValueError:
        assert True


def test_set_width():
    rect = Rectangle(5)
    rect.width = 10
    assert (rect.width == 10)


def test_set_negative_width():
    rect = Rectangle(5)
    try:
        rect.width = -10
    except NegativeValueError:
        assert True


def test_set_height():
    rect = Rectangle(3, 4)
    rect.height = 6
    assert (rect.height == 6)


def test_set_negative_height():
    rect = Rectangle(3, 4)
    try:
        rect.height = -6
    except NegativeValueError:
        assert True


def test_subtraction():
    rect_1 = Rectangle(10, 3)
    rect_2 = Rectangle(4, 1)
    rect = rect_1 - rect_2
    assert (rect == Rectangle(6, 2))


def test_subtraction_negative_result():
    rect_1 = Rectangle(3, 4)
    rect_2 = Rectangle(10, 1)
    try:
        rect = rect_1 - rect_2
    except NegativeValueError:
        assert False


def test_subtraction_same_perimeter():
    rect_1 = Rectangle(5, 1)
    rect_2 = Rectangle(4, 2)
    try:
        rect = rect_1 - rect_2
    except NegativeValueError:
        assert False
    assert (rect == Rectangle(1, 2))


if __name__ == '__main__':
    # rec_1 = Rectangle(5)
    # rec_2 = Rectangle(3, 4)
    # rec = rec_1 + rec_2
    # print(rec.width, rec.height)
    # pytest.main(["--no-header", '-q', "--durations=0", new_filename])
    # pytest.main()
    rect_1 = Rectangle(5, 1)
    rect_2 = Rectangle(4, 3)
    re = rect_1 - rect_2
    print(re.width, re.height)
