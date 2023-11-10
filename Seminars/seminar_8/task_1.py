# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки

import json
from pathlib import Path


# BASE_DIR = Path(__file__).resolve().parent # что-то с переназначением корневого каталога

def create_json_from_txt(src_file_name: str = 'task_1.txt',
                         res_file_name: str = 'task_1.json'):
    with open(src_file_name, 'r', encoding='UTF-8') as f:
        file_lines = [el.split(' | ') for el in f.readlines()]

    # print(file_lines)
    file_lines = list(map(lambda x: (x[0].title(), float(x[1])), file_lines))
    names_dict = dict(file_lines)

    with open(res_file_name, 'w', encoding='UTF-8') as f:
        json.dump(names_dict, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    create_json_from_txt()
