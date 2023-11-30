from abc import ABC


class Interface(ABC):
    """Абстрактный интерфейс пользователя"""

    def input_data(self, data: str) -> str:
        """Ввод данных"""
        pass

    def print_data(self, data: str):
        """Вывод данных"""
        pass
