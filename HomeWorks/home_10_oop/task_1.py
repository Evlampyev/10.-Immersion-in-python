class Animal:

    def __init__(self, name: str):
        self.name = name


class Bird(Animal):
    def __init__(self, name: str, wingspan: float):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return self.wingspan / 2


class Fish(Animal):

    def __init__(self, name: str, max_depth: float):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self) -> str:
        if self.max_depth < 10:
            return 'Мелководная рыба'
        elif 100 >= self.max_depth >= 10:
            return "Средневодная рыба"
        else:
            return "Глубоководная рыба"


class Mammal(Animal):

    def __init__(self, name: str, weight: float):
        super().__init__(name)
        self.weight = weight

    def category(self) -> str:
        if self.weight < 1:
            return 'Малявка'
        elif 1 <= self.weight <= 200:
            return 'Обычный'
        else:
            return 'Гигант'


class AnimalFactory:
    # def __init__(self, animal_type: str, *args):
    #     self.create_animal(animal_type, *args)
    @staticmethod
    def create_animal(animal_type, *args):
        match animal_type:
            case 'Bird':
                animal = Bird(*args)
            case 'Fish':
                animal = Fish(*args)
            case 'Mammal':
                animal = Mammal(*args)
            case _:
                raise ValueError("Don't know such an animal")
        return animal


if __name__ == '__main__':
    # Создание экземпляров животных
    animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
    animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
    animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)

    # Вывод результатов
    print(animal1.wing_length())
    print(animal2.depth())
    print(animal3.category())
