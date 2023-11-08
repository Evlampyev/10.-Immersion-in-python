# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения,
# текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы,
# которые не подошли для сортировки.

import os


def sort_files(exts_dict: dict[str, list[str]]):
    for file_name in os.listdir():
        if os.path.isfile(file_name):
            for directory, files_exts in exts_dict.items():
                if file_name.rsplit('.', 1)[1] in files_exts:
                    # rsplit -  split'ует c конца, по другому можно:
                    # file_name.rsplit('.')[-1]
                    if not os.path.isdir(directory):
                        os.mkdir(directory)
                    os.replace(file_name, os.path.join(directory, file_name))


if __name__ == '__main__':
    sort_files({
        'video': ['avi', 'mpg', 'mkv'],
        'audio': ['mp3', 'wma'],
        'texts': ['txt'],
    }
    )
