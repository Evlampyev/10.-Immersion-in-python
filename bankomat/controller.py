from card import Card
from money import Money
from bankomat import Bankomat
from terminal import Terminal as MyInteface


class Controller:
	"""Работа всей системы"""
	CHECKING_NUM = 50

	def __init__(self, money=1000):
		user_money = Money(money, "$")
		user_card = Card(user_money)
		bankomat = Bankomat()
		MyInteface.print_text("Здравствуйте")
		self.request_to_perform_operations()

	@staticmethod
	def checking_multiplicity(num) -> bool:
		"""
		Проверка на кратность 50
		:param num:
		:return: bool
		"""
		return num % Controller.CHECKING_NUM == 0

	@staticmethod
	def request_to_perform_operations() -> int:
		"""Запрос на выполнение операций"""
		lst = [
			"   Какую операцию будем выполнять: "
			"1. Пополнить баланс карты",
			"2. Снять наличные с карты",
			"3. Выйти"]
		for el in lst:
			MyInteface.print_text(el)
		choice = MyInteface.input_data()
		return choice
