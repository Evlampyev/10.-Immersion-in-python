class Money:
    def __init__(self, money: int, currency: str):
        """
        Инициализация денежной единицы
        :param money: int
        :param currency: str
        """
        self.money = money
        self.currency = currency

    def __str__(self) -> str:
        return f"{self.money}{self.currency}"

    def __le__(self, other):
        return self.money <= other.money and self.currency == other.currency

    def __lt__(self, other):
        return self.money < other.money and self.currency == other.currency

    def __eq__(self, other):
        return self.money == other.money and self.currency == other.currency

    def __gt__(self, other):
        return self.money > other.money and self.currency == other.currency

    def __ge__(self, other):
        return self.money >= other.money and self.currency == other.currency

    def __add__(self, other):
        self.money += other.money

    def __sub__(self, other):
        self.money -= other.money
