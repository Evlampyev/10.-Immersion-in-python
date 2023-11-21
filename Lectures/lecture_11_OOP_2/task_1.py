"""Дандер-метод new - инициируется при создании класса"""
class User:
    def __init__(self, name: str):
        self.name = name
        print(f'Создал {self.name = }')

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)  # вызываем родительский метод класса Object
        print(f'Создал класс {cls}')
        return instance


if __name__ == '__main__':

    print('Создаём первый раз')
    u_1 = User('Спенглер')
    print('Создаём второй раз')
    u_2 = User('Венкман')
    print('Создаём третий раз')
    u_3 = User(name='Стэнц')
