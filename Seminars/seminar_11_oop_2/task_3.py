# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

class Rectangle:

    def __init__(self, a: float, b: float = None):
        self.a = a
        self.b = a if b is None else b

    def get_area(self):
        return self.a * self.b

    def get_perimetr(self):
        return self.a * 2 + self.b * 2

    def __add__(self, other: 'Rectangle'):
        if isinstance(other, Rectangle):
            new_length = self.a + other.a
            new_width = self.b + other.b
            return Rectangle(new_length, new_width)

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            if self.get_area() > other.get_area():
                new_length = abs(self.a - other.a)
                new_width = abs(self.b - other.b)
                return Rectangle(new_length, new_width)
            else:
                raise ValueError("Вычитаемое больше уменьшаемого")
        else:
            raise TypeError("Другой объект не прямоугольник")

    def __str__(self):
        return f'Прямоугольник со сторонами {self.a} и {self.b}'


if __name__ == '__main__':
    a = Rectangle(4, 6)
    b = Rectangle(2)
    print(a)
    c = a + b
    print(f'c=a+b = {c}')
    d = a - c
    print(f'd=a-b = {d}')
