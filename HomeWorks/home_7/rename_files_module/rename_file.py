# Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:
#
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
# исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории

from pathlib import Path
import os


def rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc"):
    # print(Path.cwd())  # получение рабочего директория
    path = Path('test_folder_old')
    os.chdir(path)
    iter_list_path = Path(Path.cwd())
    count = 0
    for file in iter_list_path.iterdir():
        file_name = str(file).rsplit('\\')[-1]
        if file_name.rsplit('.')[-1] == source_ext:
            new_file_name = desired_name + new_file_number(count, num_digits) + '.' + target_ext
            count += 1
            # print(new_name)
            Path(file_name).rename(new_file_name)


def new_file_number(count: int, num: int) -> str:
    result = str(count)

    while len(result) < num:
        result = '0' + result
    return result


if __name__ == '__main__':
    rename_files("new_file_", 3, "txt", "doc")
