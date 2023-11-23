class Archive:
    _instance = None
    archive_text = []
    archive_num = []

    def __new__(cls, text: str, number: int | float):

        if cls._instance is None:
            cls.archive_text = [text]
            cls.archive_num = [number]
        else:
            cls.archive_text = cls.archive_text.copy()
            cls.archive_text.append(text)
            cls.archive_num = cls.archive_num.copy()
            cls.archive_num.append(number)
        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, text: str, number: int | float):
        self.text = text
        self.number = number
        self.archive_text = self.archive_text
        self.archive_num = self.archive_num

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_num}'


if __name__ == '__main__':
    archive1 = Archive("Запись 1", 42)
    print(archive1)
    archive2 = Archive("Запись 2", 3.14)
    print(archive2)
    print(archive1)
    archive3 = Archive('Запись 3', 777)
    print(archive3)
    print(archive1)
