import os
from pathlib import Path

os.rename('old_name.py', 'new_name.py')  # переименование файла

p = Path('old_file.py')  # переименование файла
p.rename('new_file.py')

Path('new_file.py').rename('newest_file.py')  # переименование файла

# все три метода делают одно и тоже


os.replace('newest_file.py', os.path.join(os.getcwd(), 'dir',
                                          'new_name.py'))  # перенос файла

old_file = Path('new_name.py')
new_file = old_file.replace(Path.cwd() / 'new_os_dir' / old_file) # перенос файла

# оба метода делают одно и тоже
