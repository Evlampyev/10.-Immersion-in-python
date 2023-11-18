class Person:
    max_up = 3

    def __init__(self):
        """Конструктор экземпляров класса"""
        self.level = 1
        self.health = 100
        print(f'{id(self)}')


p1 = Person()
p2 = Person()

print(f'{p1.max_up = }, {p1.level = }, {p1.health = }')
print(f'{p2.max_up = }, {p2.level = }, {p2.health = }')
# print(f'{Person.max_up = }, {Person.level = }, {Person.health =}')
# AttributeError: type object 'Person' has no attribute 'level'
Person.level = 100  # не влияет на экземпляры класса, потому что level в init
p3 = Person()
print(f'{Person.level = }, {p1.level = }, {p2.level = } {p3.level = }')
