"""чтение данных о каталогах"""

import os
from pathlib import Path

print(os.listdir())
p = Path(Path().cwd())
for obj in p.iterdir():
    print(obj)

# Функция listdir возвращает список файлов и каталогов.

# Метод iterdir у экземпляра класса Path является генератором.
# В цикле он возвращает объекты из выбранной директории.
