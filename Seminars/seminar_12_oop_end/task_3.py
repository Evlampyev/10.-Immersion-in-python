# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.

class Factorial:
    def __init__(self, start=1, stop=2, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.__prev_fact = 1
        return self

    def __next__(self):
        while self.start <= self.stop:
            self.__prev_fact *= self.start
            self.start += self.step
            return self.__prev_fact
        raise StopIteration('End of range reached')


if __name__ == '__main__':
    for el in Factorial(stop=7):
        print(el)
