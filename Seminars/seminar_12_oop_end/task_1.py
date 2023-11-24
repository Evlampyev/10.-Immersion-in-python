# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и их факториалов.

class Factorial:

    def __init__(self):
        self.storage = []
        self.last = 1
        self.count = 1

    def __call__(self, value):
        if value > self.count:
            i = self.count
            while i < value:
                self.storage.append(self.last)
                self.count += 1
                i += 1
                self.last = self.last * i
            self.storage.append(self.last)
        else:
            return self.storage[value - 1]
        return self.last

    def get_storage(self):
        return self.storage


if __name__ == '__main__':
    fact = Factorial()
    print(fact(5))
    print(fact.storage)
    print(fact.get_storage())
    print(fact(8))
    print(fact.get_storage())
    print(fact(2))
