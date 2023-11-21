# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

class Archive:
    """Архив, хранит все предыдущие экземпляры"""
    _last = []

    def __init__(self, num: int, name: str):
        """Инициализация класса"""
        self.num = num
        self.name = name
        self.archive_list = Archive._last.copy()
        Archive._last.append(self)

    def __repr__(self):
        """Вывод на экран для программистов"""
        return f'Arhive({self.num}, {self.name})'

    def __str__(self):
        """Вывод на экран для пользователя"""
        return (f'Это Архив для экземпляра {self.name} '
                f'с числом {self.num}, содержащий в себе данные {self.archive_list}')


if __name__ == '__main__':

    a = Archive(1, 'a')
    b = Archive(2, 'b')
    c = Archive(3, 'c')
    print(f'{a.archive_list = }')
    print(f'{b.archive_list = }')
    print(f'{c.archive_list = }')

    help(a)

    print(b)
    print(repr(c))

    new_a = eval(repr(c))
    print(new_a)
