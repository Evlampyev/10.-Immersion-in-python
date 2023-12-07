"""Интерфейс для работы через терминал"""
from interface import Interface


class Terminal(Interface):
    @staticmethod
    def print_text(data: str):
        print(data)

    @staticmethod
    def input_data(**kwargs):
        data: int = 0
        try:
            data: int = int(input())
        except ValueError:
            print('Не верный ввод, должно быть число')
            Terminal.input_data()
        return data

    @staticmethod
    def parser_input(self):
        return input()
