from terminal_interface import TerminalInterface
from company import Company
from user import User
from pathlib import Path
from my_error import ValueInRangeError


class Controller:
    interface = TerminalInterface()

    # directory = Path.cwd() / 'HomeWorks' / 'home_13' / 'task_5_from_seminar'

    def __init__(self):
        lst_company = self.company_in_place()
        self.interface.print_data(f'Зарегистрированные компании: {lst_company}')
        company_name = self.interface.input_data('Введите название компании: ')
        self.company = Company(company_name)

        self.choose_menu()

    def company_in_place(self):
        pathlist = Path().cwd().glob('*.json')
        company_list = []
        for el in pathlist:
            company_list.append(el.name.split('.')[0])
        return company_list

    def menu_print(self):
        lst = ['Ваши действия:',
               '1. Авторизация',
               "2. Регистрация",
               "3. Выход"]
        for el in lst:
            self.interface.print_data(el)

    def choose_menu(self):
        self.menu_print()
        menu_res = input()
        while menu_res != '3':
            match menu_res:
                case '1':
                    self.authorization()
                case '2':
                    self.registration()
            self.menu_print()
            menu_res = input()

    def authorization(self):
        print('aut')

    def registration(self):
        print('reg')
        lst_registration = ["Введите имя пользователя: ",
                            "Введите ID пользователя: ",
                            "Введите уровень доступа пользователя: "]
        name = self.interface.input_data(lst_registration[0])
        u_id = self.interface.input_data(lst_registration[1])
        while self.company.check_id_in_company(u_id):
            u_id = self.interface.input_data('Пользователь с таким ID существует, введите новый: ')
        level_access = int(self.interface.input_data(lst_registration[2]))

        try:
            user = User(name, u_id, level_access)
        except ValueInRangeError(1, 7) as error:
            self.interface.print_data(error)
            level_access = int(self.interface.input_data('Повторите ввод уровня доступа: '))
        finally:
            user = User(name, u_id, level_access)
        self.company.add_user(user)
