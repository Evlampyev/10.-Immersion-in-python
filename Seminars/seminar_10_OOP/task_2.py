# Создайте класс прямоугольник. Класс должен принимать длину и ширину при создании
# экземпляра. У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

class Rectangle:
    def __init__(self, *args):
        self.a = args[0]
        self.b = args[1] if len(args) == 2 else args[0]

    def get_area(self):
        return self.a * self.b

    def get_perimetr(self):
        return self.a * 2 + self.b * 2


if __name__ == '__main__':
    rectangle = Rectangle(2, 3)
    square = Rectangle(3)
    print(f'{rectangle.get_area() = }')
    print(f'{rectangle.get_perimetr() = }')
    print(f'{square.get_area() = }')
    print(f'{square.get_perimetr() = }')
