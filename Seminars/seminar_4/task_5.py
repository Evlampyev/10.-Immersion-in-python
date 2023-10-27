# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

def dict_money(name: list[str],
               bet: list[int],
               prize: list[str]) -> dict[str, float]:
    result = dict()
    for i in range(len(name)):
        result[name[i]] = bet[i] * float(prize[i][:-1]) / 100
    return result


def f(name: list[str],
      stavka: list[int],
      pr: list[str]):
    pr = list(map(lambda x: float(x[:-1]), pr))  # создание нового списка \
    # вместо str теперь float
    return {i[0]: i[1] * i[2] / 100 for i in zip(name, stavka, pr)}


my_name = ['Игорь', 'Павел', 'Нина']
my_bet = [1000, 1200, 1350]
my_prize = ['10.25%', '12%', '13.8%']

print(my_name, my_bet, my_prize)
print(dict_money(my_name, my_bet, my_prize))
print(f(my_name, my_bet, my_prize))
