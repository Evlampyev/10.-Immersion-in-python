from user import User
import json
from pathlib import Path


class Company:
    # directory = Path.cwd() / 'HomeWorks' / 'home_13' / 'task_5_from_seminar'

    def __init__(self, name_company: str):
        self.name_company = name_company
        self.file_name = f'{name_company}' + '.json'

    @property
    def users_dict(self) -> dict:
        """Получение словаря пользователей из json"""
        if not Path(self.file_name).exists():  # проверка на существование файла
            return dict()
        else:
            with open(self.file_name, 'r', encoding='UTF-8') as file:
                json_file = json.load(file)  # загрузка JSON из файла и сохранение в dict
                return json_file

    @users_dict.setter
    def users_dict(self, my_dict: dict):
        """Сохранение словаря пользователей в json файл"""
        with open(self.file_name, 'w') as file:
            json.dump(my_dict, file, indent=4, ensure_ascii=False)

    def from_dict_to_list(self):
        """Преобразование из словаря в список User"""
        my_dict = self.users_dict
        my_list = []
        for level, name_u_id_dict in my_dict.items():
            for u_id, name in name_u_id_dict.items():
                my_list.append(User(name, u_id, int(level)))
        return my_list

    def check_id_in_company(self, u_id: str) -> bool:
        """Проверка наличия ID пользователя в компании"""
        lst_id = []
        company_list = self.from_dict_to_list()
        for user in company_list:
            lst_id.append(user.u_id)
        return u_id in lst_id

    def add_user(self, user):
        """Добавление нового сотрудника в компанию"""
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
