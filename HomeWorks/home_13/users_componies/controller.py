from .terminal_interface import TerminalInterface
from .company import Company
from .user import User
from pathlib import Path
from .my_error import ValueInRangeError, LevelException, VerificationError


class Controller:
    interface = TerminalInterface()

    # directory = Path.cwd() / 'HomeWorks' / 'home_13' / 'task_5_from_seminar'

    def __init__(self):
        self.company = ''
        self.begin_work_with_company()

    def begin_work_with_company(self):
        lst_company = self.company_in_place()
        self.interface.print_data(f'Зарегистрированные компании: {lst_company}')
        company_name = self.interface.input_data('Введите название компании: ')
        if company_name in lst_company:
            self.company = Company(company_name, 0)
            self.interface.print_data(f'Уровень доступа вашей '
                                      f'организации: {self.company.access_level}.')
        else:
            access_level = int(self.interface.input_data('Уровень доступа '
                                                         'для сотрудников компании: '))
            self.company = Company(company_name, access_level)

        self.choose_menu()

    @staticmethod
    def company_in_place():
        path = Path().cwd() / 'companies'
        pathlist = path.glob('*.json')
        company_list = []
        for el in pathlist:
            company_list.append(el.name.split('.')[0])
        return company_list

    def menu_print(self):
        lst = ['Ваши действия:',
               '1. Авторизация',
               "2. Регистрация",
               "3. Посмотреть список сотрудников",
               "4. Сменить компанию",
               "0. Выход"]
        for el in lst:
            self.interface.print_data(el)

    def choose_menu(self):
        self.menu_print()
        menu_res = input()
        while menu_res != '0':
            match menu_res:
                case '1':
                    self.authorization()
                case '2':
                    self.registration()
                case '3':
                    self.interface.print_data(f'{self.company}')
                case '4':
                    self.begin_work_with_company()
                case _:
                    self.interface.print_data('Нет такого пункта меню')

            self.menu_print()
            menu_res = input()

    def authorization(self):
        self.interface.print_data('-- Авторизация --')
        lst_authorization = ["Введите имя пользователя: ", "Введите ID пользователя: "]
        name = self.interface.input_data(lst_authorization[0])
        u_id = self.interface.input_data(lst_authorization[1])
        auth_user = User(name, u_id, 1)
        try:
            user_level = self.company.user_verification(auth_user)
            self.interface.print_data(f'Авторизация успешна, '
                                      f'ваш уровень доступа {user_level}')
        except VerificationError as error:
            self.interface.print_data(error)

    def registration(self):
        self.interface.print_data('-- Регистрация --')
        lst_registration = ["Введите имя пользователя: ",
                            "Введите ID пользователя: ",
                            "Введите уровень доступа пользователя: "]
        name = self.interface.input_data(lst_registration[0])
        u_id = self.interface.input_data(lst_registration[1])
        while self.company.check_id_in_company(u_id):
            u_id = self.interface.input_data('Пользователь с таким ID существует, '
                                             'введите новый: ')
        level_access = int(self.interface.input_data(lst_registration[2]))
        error = True
        while error:
            try:
                error = False
                user = User(name, u_id, level_access)
            except ValueInRangeError as value_error:
                error = True
                self.interface.print_data(value_error)
                level_access = int(
                    self.interface.input_data('Повторите ввод уровня доступа: '))
        try:
            self.company.add_user(user)
        except LevelException as lev_er:
            self.interface.print_data(lev_er)
