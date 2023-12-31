from .user import User
import json
from pathlib import Path
from .my_error import LevelException, VerificationError
from typing import Any


class Company:
    # directory = Path.cwd() / 'HomeWorks' / 'home_13' / 'task_5_from_seminar'

    def __init__(self, name_company: str, access_level: int):
        self.name_company = name_company
        self.file_name = f'{name_company}' + '.json'
        if access_level > 0:
            self.access_level = access_level
            self.users_dict = {0: {name_company: access_level}}
        else:
            company = self.users_dict['0']
            self.access_level = company[name_company]

    @property
    def users_dict(self) -> dict:
        """Получение словаря пользователей из json"""
        path = Path('companies', self.file_name)
        if not Path(path).exists():  # проверка на существование файла
            return dict()
        else:
            with open(path, 'r', encoding='UTF-8') as file:
                json_file = json.load(file)  # загрузка JSON из файла и сохранение в dict
                return json_file

    @users_dict.setter
    def users_dict(self, my_dict: dict):
        """Сохранение словаря пользователей в json файл"""
        path = Path.cwd() / 'companies'
        if not path.exists():
            Path('companies').mkdir()
        path = Path('companies', self.file_name)
        with open(path, 'w') as file:
            json.dump(my_dict, file, indent=4, ensure_ascii=False)

    def from_dict_to_list(self) -> list[User]:
        """Преобразование из словаря в список User"""
        my_dict = self.users_dict
        my_list = []
        for level, name_u_id_dict in my_dict.items():
            for u_id, name in name_u_id_dict.items():
                if level != '0':
                    my_list.append(User(name, u_id, int(level)))
        return my_list

    def check_id_in_company(self, u_id: str) -> bool:
        """Проверка наличия ID пользователя в компании"""
        lst_id = []
        company_list = self.from_dict_to_list()
        for user in company_list:
            lst_id.append(user.u_id)
        return u_id in lst_id

    def user_verification(self, user) -> Any:
        users_list = self.from_dict_to_list()
        user_access_level = None
        for el in users_list:
            if el == user:
                user_access_level = el.level_access
        if user_access_level is None:
            raise VerificationError(user.name)
        else:
            return user_access_level

    def add_user(self, user: User):
        """Добавление нового сотрудника в компанию"""
        if user.level_access < self.access_level:
            raise LevelException(self.access_level)
        else:
            users_dict = self.users_dict
            if str(user.level_access) in users_dict:
                users_dict[str(user.level_access)][user.u_id] = user.name
            else:
                users_dict[user.level_access] = {user.u_id: user.name}
            self.users_dict = users_dict

    def __str__(self):
        """Вывод списка пользователей компании"""
        my_list = self.from_dict_to_list()
        result = f'Список сотрудников компании "{self.name_company}": \n'
        for el in my_list:
            result = result + f'{el}\n'
        if result == '':
            return f"В компании {self.name_company} нет сотрудников"
        else:
            return result
