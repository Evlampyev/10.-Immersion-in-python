import os
from pathlib import Path

print(os.getcwd())  # получение рабочего директория
print(Path.cwd())  # получение рабочего директория
os.chdir('../..')  # изменение рабочего директория
print(os.getcwd())
print(Path.cwd())

os.mkdir('new_os_dir')  # создание каталога new_os_dir
Path('new_path_dir').mkdir()  # создание каталога new_path_dir

os.makedirs('dir/other_dir/new_os_dir')  # создание вложенных директорий
Path('some_dir/dir/new_path_dir').mkdir()  # FileNotFoundError
Path('some_dir/dir/new_path_dir').mkdir(parents=True)
# создание вложенных директорий, параметр в скобках указывает
# на создание всех родителей


# os.rmdir('dir') # OSError - невозможность удаления не пустых папок
# Path('some_dir').rmdir() # OSError  - невозможность удаления не пустых папок
os.rmdir('dir/other_dir/new_os_dir')
Path('some_dir/dir/new_path_dir').rmdir()


import shutil

shutil.rmtree('dir/other_dir') # удаление всего дерева от other_dir и ниже
