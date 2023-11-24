"""Менеджер контекста"""

import sqlite3


class DB:
    """ Класс для работы с БД"""

    def __init__(self, name):
        self.name = name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        """Установка соединения с БД"""
        self.connection = sqlite3.connect(self.name)  # установка соединения
        self.cursor = self.connection.cursor()  # получаю курсор
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        # exc_type - тип ошибки, если она произойдет внутри менеджера контента
        # exc_val - текст, который хранится внутри ошибки
        # exc_tb - текст троссировки, весь набор действий, которые привели к ошибке
        self.connection.commit()  # подтверждение изменений
        self.connection.close()  # закрытие соединение
        self.cursor = self.connection = None  # мы ушли в исходное состояние


if __name__ == '__main__':

    db = DB('sqlite.db')
    with db as cur:  # AttributeError: __exit__ если нет метода exit
        cur.execute("""create table if not exists users(name, age);""")
        cur.execute("""insert into users values ('Гвидо', 66);""")
