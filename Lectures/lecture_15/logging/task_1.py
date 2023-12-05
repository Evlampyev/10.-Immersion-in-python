import logging

logging.basicConfig(level=logging.NOTSET)  # использовать все уровни логирования

logging.debug('Очень подробная отладочная информация. Заменяем множество "принтов"')
logging.info('Немного информации о работе кода')
logging.warning('Внимание! Надвигается буря!')
logging.error('Поймали ошибку. Дальше только неизвестность')
logging.critical('На этом всё')


#так обычно не используют напрямую командыо через loggint делают как в task_2