# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# 📌 Соберите информацию о содержимом в виде объектов namedtuple.
# 📌 Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.

from argparse import ArgumentParser
from collections import namedtuple
from pathlib import Path
from logging import basicConfig, getLogger, INFO

if __name__ == '__main__':
    parser = ArgumentParser(description="Получение пути папки")
    parser.add_argument('path', type=str, nargs=1, help='Введите путь до папки')
    args = parser.parse_args()

    basicConfig(filename='log.log', filemode='w', encoding='utf-8', level=INFO,
                format='{levelname:<8} - {asctime}, {msg}',
                style='{')
    logger = getLogger(__name__)

    Files = namedtuple('Files', ['name', 'extension', 'flag', 'parent_dir'])
    if Path(args.path[0]).exists():
        user_dir = Path(args.path[0])
        logger.info(f'Рассматриваемый каталог: {user_dir}')
        file_list = []
        for obj in user_dir.iterdir():
            if obj.is_file():
                file = Files(obj.name.split('.')[0], obj.name.split('.')[1], 'file',
                             obj.parent)
            else:
                file = Files(obj.name, None, 'dir', obj.parent)
            file_list.append(file)
            logger.info(f'Объект {file} добавлен')
    else:
        print(f"Пути {args.path[0]} нет")
    print('см. логи')
