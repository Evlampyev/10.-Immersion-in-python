import logging
from other import log_all

logging.basicConfig(filename='project.log.', filemode='w', encoding='utf-8',
                    level=logging.INFO)  # 'w'- каждый раз заново файл заполняется,
# если не указано, до будет дописываться

logger = logging.getLogger('Основной файл проекта')
logger.warning('Внимание! Используем вызов функции из другого модуля')
log_all()
