# Создайте три (или более) отдельных классов животных. Например, рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные
# для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

class Animal:
    def __init__(self, name: str, age: int, weight: float, breed: str) -> object:
        self.name = name
        self.age = age
        self.weight = weight
        self.breed = breed
        self.special = None

    def get_special(self):
        return self.special

    def animal_say(self):
        pass

    def __str__(self):
        return f'Кличка: {self.name}, возраст: {self.age}, масса: {self.weight} кг'


class Bird(Animal):
    def __init__(self, name: str, age: int, weight: float, breed: str, wingspan: float,
                 legs: int = 2):
        super().__init__(name, age, weight, breed)
        self.special = {
            'wingspan': wingspan,
            'legs'    : legs,
        }

    def animal_say(self):
        return f'Кря-кря'


class Dog(Animal):

    def __init__(self, name: str, age: int, weight: float, breed: str, color: str,
                 legs: int = 4):
        super().__init__(name, age, weight, breed)
        self.special = {
            'color': color,
            'legs' : legs
        }

    def animal_say(self):
        return f'гав-гав'


if __name__ == '__main__':
    dog = Dog('Рекс', 4, 5.600, 'Овчарка', 'Черный')
    print(dog)
    print(f'{dog.special = }')
    print(dog.animal_say())

    bird = Bird('Птица', 2, 1.400, "Синичка", 0.42)
    print(bird)
