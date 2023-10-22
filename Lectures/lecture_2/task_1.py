"""Задача"""
data: str = input("Введите текст: ")
print(f"тип - {type(data)}, адрес - {id(data)}, хеш - {hash(data)}")
