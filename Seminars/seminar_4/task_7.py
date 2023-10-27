# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.


def profit(
        companies: dict[str, list[int]]) -> bool:  # этот вариант более лучший
    for value in companies.values():
        if sum(value) < 0:
            return False
    return True


def is_all_profitable(companies: dict) -> bool:
    return all(sum(profit) > 0 for profit in companies.values())


def another_profit(
        companies: dict[str, list[int]]) -> bool:  # самая долгая функция
    profit_list = list(map(sum, companies.values()))
    return all(map(lambda x: x >= 0,
                   profit_list))  # all - коньюнкция, any - дизьюнкция


comp = {
    'MMM'   : [-12, 4, 76, 9, -5],
    'Mack'  : [-23, -45, -7, 8],
    'Cosmos': [12, 34, 56, 7],
}
print(profit(comp))
print(another_profit(comp))
print(is_all_profitable(comp))
