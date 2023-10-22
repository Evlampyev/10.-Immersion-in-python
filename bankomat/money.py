class Money:
    def __init__(self, money: int, symbol: str):
        """
        Инициализация денежной единицы
        :type symbol: object
        """
        self.money = money
        self.symbol = symbol

    def __str__(self) -> str:
        return f"{self.money}{self.symbol}"
