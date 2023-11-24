import sqlite3

connection = sqlite3.connect('sqlite.db')  # соединение с БД, если её нет, то она создастся
cursor = connection.cursor()  # получаем курсор
cursor.execute("""create table if not exists users(name, age);""")  # создаем таблицу
cursor.execute("""insert into users values ('Гвидо', 66);""")  # вносим запись в таблицу
connection.commit()  # подтверждаем изменения
connection.close()  # Закрываем соединение
