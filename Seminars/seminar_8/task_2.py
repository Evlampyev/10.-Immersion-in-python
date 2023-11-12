# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

from pathlib import Path
import json

FILE_NAME = 'task_2.json'


def get_all_users() -> dict:
    """Получение всех пользователей из файла в словарь"""
    if not Path(FILE_NAME).exists():
        return dict()
    else:
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            json_file = json.load(f)
            # загрузка JSON из файла и сохранение в dict
        return json_file


def set_all_users(new_dict: dict) -> None:
    """
    Запись в файл нового словаря пользователей
    :param new_dict: словарь пользователей
    :return: None
    """
    with open(FILE_NAME, 'w') as f:
        json.dump(new_dict, f, indent=4, ensure_ascii=False)


def check_user_level(lvl: str) -> bool:
    """Проверка на правильность ввода уровня пользователя"""
    if not (lvl.isdigit() and 0 < int(lvl) < 8):
        return True


def add_new_users(all_us: dict, us_level: str, us_id: str,
                  us_name: str) -> dict:
    """Добавление нового пользователя в словарь"""
    if us_level in all_us:
        all_us[us_level][us_id] = us_name
    else:
        all_us[us_level] = {us_id: us_name}
    return all_us


def check_user_id(all_us: dict, id_us: int) -> bool:
    """
    Проверка наличия id в исходном словаре
    :param all_us: словарь пользователей
    :param id_us: проверяемый id пользователя
    :return:
    """
    id_list = []
    for user in all_us.values():
        id_list.extend(user)
    # принимает в качестве параметра итерируемый объект
    # и объединяет его со списком.
    return id_us in id_list


def main():
    all_users = get_all_users()
    print(all_users)
    while True:

        user_name = input('Введите имя или Enter для выхода: ')
        if not user_name:
            break

        user_id = input("Введите id: ")
        while check_user_id(all_users, user_id):
            user_id = input(f'ID {user_id} уже занят, выберите другой ID: ')

        user_level = input('Введите уровень доступа пользователя: ')
        while check_user_level(user_level):
            user_level = input('Ошибка уровня доступа, '
                               ' введите число от 1 до 7: ')

        all_users = add_new_users(all_users, user_level, user_id, user_name)
        set_all_users(all_users)


if __name__ == '__main__':
    main()
