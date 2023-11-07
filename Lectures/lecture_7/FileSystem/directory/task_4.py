"""Получение информации об объектах"""
import os
from pathlib import Path

dir_list = os.listdir()
for obj in dir_list:
    print(f'{os.path.isdir(obj) = }', end='\t')
    print(f'{os.path.isfile(obj) = }', end='\t')
    print(f'{os.path.islink(obj) = }', end='\t')
    print(f'{obj = }')

p = Path(Path().cwd())
for obj in p.iterdir():
    print(f'{obj.is_dir() = }', end='\t')
    print(f'{obj.is_file() = }', end='\t')
    print(f'{obj.is_symlink() = }', end='\t')
    print(f'{obj = }')
# Обратите внимание, что при работе с модулем os мы получаем объекты str типа.
# Строки передаются в другие функции для получения результата.
# При работе с pathlib мы итерируемся по объектам Path. А если быть точным по
# экземплярам класс Path той операционной системы, в которой работает код.
# Методы проверки принадлежности являются частью экземпляра.