"""Абстрактный интерфейс пользователя"""
from abc import ABC


class Interface(ABC):

    @staticmethod
    def print_text(data: str) -> None:
        """Вывод текста"""
        pass

    @staticmethod
    def input_data(self) -> int:
        """
        Получение суммы
        :return: money
        """
        pass
