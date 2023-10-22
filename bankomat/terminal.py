"""Интерфейс для работы через терминал"""
from interface import Interface


class Terminal(Interface):
    @staticmethod
    def print_text(data: str):
        print(data)

    @staticmethod
    def input_data():
        money: int = int(input())
        return money
