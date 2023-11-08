# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона

from random import randint, choices, randbytes
from string import ascii_letters
import os


def create_filename(min_len: int = 6, max_len: int = 30) -> str:
    file_name = ''
    file_name_len = randint(min_len, max_len)
    file_name = ''.join(choices(ascii_letters, k=file_name_len))
    return file_name


def create_inner_file(min_bytes: int = 256, max_bytes: int = 4096):
    file_bytes = randint(min_bytes, max_bytes)
    return randbytes(file_bytes)


def create_files(files_ext: str = 'txt', files_count: int = 42,
                 min_bytes: int = 256, max_bytes: int = 4096,
                 min_len: int = 6, max_len: int = 30):
    if os.path.isdir('new_os_dir'):
        os.chdir('new_os_dir')
    else:
        os.mkdir('new_os_dir')
        os.chdir('new_os_dir')
    for _ in range(files_count):
        with open('.'.join((create_filename(min_len, max_len), files_ext)),
                  'wb') as f:
            f.write(create_inner_file(min_bytes, max_bytes))


create_files('12', 5)
