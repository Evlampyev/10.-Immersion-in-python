# Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле
# запрашивали имя, личный идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует
# множество пользователей.

from pathlib import Path
import json


class AccessLevel:
    def __init__(self, minimum: int = 1, maximum: int = 7):
        self.min = minimum
        self.max = maximum

    def validate(self, value: str):
        if not value.isdigit():
            raise ValueError(f'Не числовое значение')
        elif self.min >= int(value) >= self.max:
            raise ValueError(
                f'Значение не попадает в казанный промежуток от {self.min} до {self.max}')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.name, value)


class User:
    access_level = AccessLevel()

    def __init__(self, name: str, u_id: str, access_level: str):
        self.u_id = u_id
        self.name = name
        self.access_level = access_level

    def __str__(self):
        return (f'Пользователь {self.name}, UId = {self.u_id}, '
                f'уровень доступа: {self.access_level}')


class UsersCompany:

    def __init__(self, company_name: str):
        self.company_name = company_name
        self.file_name = company_name + '.json'
        self.all_users_dict = self.get_all_users()
        self.all_users = []
        self.dict_to_list()

    def get_all_users(self) -> dict:
        """Получение всех пользователей из файла в словарь"""
        if not Path(self.file_name).exists():
            return dict()
        else:
            with open(self.file_name, 'r', encoding='utf-8') as f:
                json_file = json.load(f)
                # загрузка JSON из файла и сохранение в dict
            return json_file

    def set_all_users(self) -> None:
        """Запись в файл нового словаря пользователей"""
        with open(self.file_name, 'w') as f:
            json.dump(self.all_users_dict, f, indent=4, ensure_ascii=False)

    def add_new_users(self, user: User):
        """Добавление нового пользователя в словарь"""
        if user.access_level in self.all_users_dict:
            self.all_users_dict[user.access_level][user.u_id] = user_name
        else:
            self.all_users_dict[user_level] = {user.u_id: user.name}

    def check_user_id(self, id_us: str) -> bool:
        """
        Проверка наличия id в исходном словаре
        :param id_us: проверяемый id пользователя
        :return: bool
        """
        id_list = []
        for user in self.all_users_dict.values():
            id_list.extend(user)
        # принимает в качестве параметра итерируемый объект
        # и объединяет его со списком.
        return id_us in id_list

    def dict_to_list(self):
        for level, id_name_dict in self.all_users_dict.items():
            for u_id, name in id_name_dict.items():
                user_to_list = User(name, u_id, level)
                self.all_users.append(user_to_list)

    def __str__(self):
        """Вывод списка всей компании"""
        result = ''
        for user in self.all_users:
            result = result + f'{user}' + '\n'
        return result


if __name__ == '__main__':
    new_company = UsersCompany('Helix')
    print(new_company.all_users_dict)
    print(new_company)
    check_company = new_company
    while True:

        user_name = input('Введите имя или Enter для выхода: ')
        if not user_name:
            break

        user_id = input("Введите id: ")
        while check_company.check_user_id(user_id):
            user_id = input(f'ID {user_id} уже занят, выберите другой ID: ')

        user_level = input('Введите уровень доступа пользователя: ')
        while True:
            try:
                new_user = User(user_name, user_id, user_level)
                break
            except ValueError:
                user_level = input('Ошибка уровня доступа, '
                                   ' введите число от 1 до 7: ')
        check_company.add_new_users(new_user)
        check_company.set_all_users()
