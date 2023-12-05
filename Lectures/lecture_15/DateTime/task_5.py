from datetime import datetime

dt = datetime(year=2007, month=6, day=15, hour=2, minute=14,
              microsecond=24)
print(dt)
print(dt.timestamp())  # информация о дате и времени от начала времен
print(dt.isoformat())  # вывод даты и времени с использованием 'T'
print(dt.weekday())  # выводит номер дня недели (0 - пнд, 6 - вс)
print(dt.strftime('Дата %d %B %Y. День недели %A. Время %H:%M:%S. '
                  'Это %W неделя и %j день года.'))
