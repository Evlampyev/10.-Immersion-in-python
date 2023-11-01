# Напишите однострочный генератор словаря, который принимает на вход три списка
# одинаковой длины: имена str, ставка int, премия str с указанием процентов
# вида 10.25%. В результате result получаем словарь с именем в качестве ключа
# и суммой премии в качестве значения. Сумма рассчитывается как ставка
# умноженная на процент премии. Не забудьте распечатать в конце результат.

names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]


def gen_dict(list_names: list[str], list_salary: list[int],
             list_bonus: list[str]) -> dict:
    result = {list_names[i]: list_salary[i] / 100 * int(list_bonus[i][:-1]) for
              i in
              range(len(list_names))}
    return result


print(gen_dict(names, salary, bonus))
