"""
Получение значения атрибута, __getattribute__
Присвоение атрибуту значения, __setattr__
"""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __getattribute__(self, item):
        """Получение значения атрибута"""
        if item == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        """Присвоение атрибуту значения"""
        if key == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__setattr__(self, key, value)

    def __getattr__(self, item):
        """Обращение к несуществующему атрибуту"""
        # Мы установили возврат None для любого свойства, которое не удалось найти. Метод
        # возвращает None и для свойства z, перехватывая исключение.
        return None

    def __delattr__(self, item):
        """Удаление атрибута"""
        if item in ('x', 'y'):
            setattr(self, item, 0)
        else:
            object.__delattr__(self, item)


if __name__ == '__main__':

    a = Vector(2, 4)
    print(a.z)  # AttributeError: У нас вектор на плоскости, а не в пространстве
    print(f'{a = }')
    a.z = 73  # AttributeError: У нас вектор на плоскости, а не в пространстве
    a.x = 3
    print(f'{a = }')
# Если свойство отсутствует, в первую очередь вызывается дандер __getattribute__. В
# случае возврата им ошибки AttributeError вызывается метод __getattr__. Он также
# может поднять ошибку. А может как-то иначе обработать запрос.
    print('*'*20)
    a = Vector(2, 4)
    a.s = 73
    print(f'{a = }, {a.s = }')
    del a.x
    del a.s
    print(f'{a = }, {a.s = }')