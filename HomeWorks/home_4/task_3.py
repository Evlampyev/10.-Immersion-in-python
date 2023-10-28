"""Task_3_text.md"""
import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(100)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)


def check_multiplicity(amount):
    """Проверка кратности суммы при пополнении и снятии."""
    if amount % MULTIPLICITY == 0:
        return True
    else:
        return False


def deposit(amount):
    """Пополнение счёта."""
    if check_multiplicity(amount):
        global bank_account
        bank_account += amount
        operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')
    else:
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')


def withdraw(amount):
    """Снятие денег."""
    if check_multiplicity(amount):
        global bank_account
        percent = decimal.Decimal(PERCENT_REMOVAL * amount, 0)
        amount_plus_percent = (amount + percent)
        if bank_account >= amount_plus_percent:
            bank_account -= amount_plus_percent
            operations.append(
                f'Снятие с карты {amount} у.е. Процент за снятие {percent} у.е.. Итого {bank_account} у.е.')
        else:
            operations.append(
                f'Недостаточно средств. Сумма с комиссией {amount_plus_percent} у.е. На карте {bank_account} у.е.')
    else:
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')


def exit():
    """Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях."""
    global bank_account
    if bank_account > RICHNESS_SUM:
        rich_tax = decimal.Decimal(RICHNESS_PERCENT * bank_account)
        bank_account -= rich_tax
        operations.append(
            f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {rich_tax} у.е. Итого {bank_account} у.е.')
    operations.append(f'Возьмите карту на которой {bank_account} у.е.')


bank_account = decimal.Decimal(0)
count = 0
operations = []

deposit(1000)
withdraw(200)
exit()


print(operations)
