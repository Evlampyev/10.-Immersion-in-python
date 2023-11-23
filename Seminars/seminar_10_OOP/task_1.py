# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.
from math import pi


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self) -> float:
        """Возвращает площадь окружности"""
        return pi * self.radius *self.radius

    def get_length(self) -> float:
        """Возвращаешь длину окружности"""
        return 2 * pi * self.radius


if __name__ == '__main__':
    circle = Circle(10)
    print(f'{circle.get_area() = }')
    print(f'{circle.get_length() = }')

