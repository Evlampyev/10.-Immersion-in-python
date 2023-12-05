# 📌 Функция получает на вход текст вида:
# “1-й четверг ноября”,
# “3я среда мая” и т.п.
# 📌 Преобразуйте его в дату в текущем году.
# 📌 Логируйте ошибки, если текст не соответсвует формату.

from datetime import date, datetime
from logging import getLogger, basicConfig, NOTSET

WEEKDAYS = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота',
            'воскресенье']
MONTHS = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа',
          'сентября', 'октября', 'ноября', 'декабря']


def convert_to_date(formatted_date: str) -> date | None:
    week, weekday, month = formatted_date.split()
    try:
        weekday = WEEKDAYS.index(weekday)
    except ValueError:
        LOGGER.error(f'Не верный формат. Нет такого дня недели {weekday}')
        return
    try:
        month = MONTHS.index(month) + 1
    except ValueError:
        LOGGER.error(f'Не верный формат. Нет такого месяца {month}')
        return
    week = int(week.split('-')[0])
    if int(week) > 5:
        LOGGER.error(f'Не верный формат. Неделя должна быть <=5')
        return

    first_month_day = date(year=date.today().year, month=month, day=1)
    print(first_month_day.weekday())
    if first_month_day.weekday() <= weekday:
        month_day = (week - 1) * 7 + weekday - first_month_day.weekday() + 1
    else:
        month_day = (week - 1) * 7 + weekday - first_month_day.weekday() + 8

    return datetime.strptime(f'{month_day} {month} {date.today().year}',
                             '%d %m %Y').date()


if __name__ == '__main__':
    basicConfig(filename='log/log_3.log',
                level=NOTSET,
                # datefmt='%H:%M:%S',
                format='[{levelname:<8}] {asctime}: {funcName} -> {msg}',
                style='{')
    LOGGER = getLogger(__name__)

    print(convert_to_date('3-й додж февраля'))
