date_to_prove = '0.5.2022'

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


def is_possible_data(data: str) -> bool:
    day, month, year = map(int,
                           data.split(
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


print(is_possible_data(date_to_prove))
