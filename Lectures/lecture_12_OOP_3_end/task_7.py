class User:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


if __name__ == '__main__':
    user = User('Alex')
    print(f'{user.name = }')
    user.name = 'Sasha' # AttributeError: property 'name' of 'User' object has no setter
    # потому что name можно получить, а изменить нельзя
    print(f'{user.name = }')
