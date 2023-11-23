from functools import total_ordering


@total_ordering
class Rectangle:
    def __init__(self, width: int, height: int = None):
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
            return Rectangle(abs(self.width - other.width), abs(self.height - other.height))

    def __lt__(self, other):
        return self.area() < other.area()

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __str__(self):
        return f'Прямоугольник со сторонами {self.width} и {self.height}'


if __name__ == '__main__':
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(3, 7)

    print(f"Периметр rect1: {rect1.perimeter()}")
    print(f"Площадь rect2: {rect2.area()}")
    print(f"rect1 < rect2: {rect1 < rect2}")
    print(f"rect1 == rect2: {rect1 == rect2}")
    print(f"rect1 <= rect2: {rect1 <= rect2}")

    rect3 = rect1 + rect2
    print(f"Периметр rect3: {rect3.perimeter()}")
    rect4 = rect1 - rect2
    print(f"Ширина rect4: {rect4.width}")
