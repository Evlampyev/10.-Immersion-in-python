"""Представление для создания экземпляра __repr__"""


class User:
    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()

    def __repr__(self):
        return f'User({self.name})'


class AnotherUser:
    def __init__(self, name: str, equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment is not None else []
        self.life = 3

    def __repr__(self):
        return f'AnotherUser({self.name}, {self.equipment})'


if __name__ == '__main__':

    user = User('Спенглер')
    print(user)

    new_user = AnotherUser('Венкман', ['протонный ускоритель', 'ловушка'])
    print(new_user)
