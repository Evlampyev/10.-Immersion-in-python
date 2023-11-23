# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)
from time import time


class MyStr(str):

    def __new__(cls, data: str, author: str):
        instance = super().__new__(cls, data)
        instance.author = author
        instance.creation_time = time()
        return instance


if __name__ == '__main__':
    mstr = MyStr('qwe', 'Dis_Bro')
    print(mstr)
    print(mstr.author)
    print(mstr.creation_time)
