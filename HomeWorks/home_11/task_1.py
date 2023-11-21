from datetime import datetime


class MyStr(str):

    def __new__(cls, value: str, author: str):
        instance = super().__new__(cls)
        instance.value = value
        instance.author = author
        instance.time = datetime.now().strftime("%Y-%m-%d %H:%M")
        return instance

    def __str__(self):
        return f'{self.value} (Автор: {self.author}, Время создания: {self.time})'

    def __repr__(self):
        return f"MyStr('{self.value}', '{self.author}')"


if __name__ == '__main__':
    event = MyStr("Завершилось тестирование", "John")
    print(event)
