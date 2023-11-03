# Создайте модуль и напишите в нём функцию, которая получает на вход дату
# в формате DD.MM.YYYY
# � Функция возвращает истину, если дата может существовать или ложь,
# если такая дата невозможна.
# � Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# � Весь период (1 января 1 года - 31 декабря 9999 года) действует
# Григорианский календарь.
# � Проверку года на високосность вынести в отдельную защищённую функцию.

YEAR_BOUND = (1, 9999)
MONTH_DAYS = {
    1 : 31,
    2 : (28, 29),
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10: 31,
    11: 30,
    12: 31
}


def _is_leap_year(year: int) -> bool:
    """Проверка года на високосность"""
    return not year % 4 and year % 100 or not year % 400


def is_possible_data() -> bool:
    day, month, year = map(int,
                           input("Введите дату в формате DD.MM.YYYY: ").split(
                               '.'))
    if YEAR_BOUND[0] <= year <= YEAR_BOUND[1]:
        if month in MONTH_DAYS:
            if month == 2 and _is_leap_year(year):
                max_days = MONTH_DAYS[month][1]
            elif month == 2:
                max_days = MONTH_DAYS[month][0]
            else:
                max_days = MONTH_DAYS[month]
            if day in range(1, max_days + 1):
                return True
    return False


if __name__ == '__main__':
    print(is_possible_data())
