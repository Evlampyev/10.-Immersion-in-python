import logging
from other import log_all

FORMAT = ('{levelname:<8} - {asctime}. В модуле "{name}" в строке {lineno:03d} '
          'функция "{funcName}()" в {created} секунд записала сообщение: {msg}')
# FORMAT - передаёт уровень логирования и время записи в читаемом формате
# asctime - время в которое произошло событие
# name -
# lineno: 03d - номер строки в которой вызван логгер
# funcName - имя функции, внутри которой вызван логгер
# created - время в секундах, в которое произошло событие, от начала времен (1.01.1970)
# msg - сообщение логгера


logging.basicConfig(format=FORMAT, style='{', level=logging.INFO)  # style='{' относится
# к формату, чтобы мы правильно его расшифровали
logger = logging.getLogger('main')
logger.warning('Внимание! Используем вызов функции из другого модуля')
log_all()
