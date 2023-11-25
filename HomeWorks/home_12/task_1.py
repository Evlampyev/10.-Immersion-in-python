import csv


class Fio:

    @classmethod
    def validate_text(cls, value):
        if not isinstance(value, str):
            raise TypeError("Тип данных не строка")
        lst = value.split()
        for el in lst:
            if not el.isalpha() or not el.istitle():
                raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate_text(value)
        return setattr(instance, self.name, value)


class Range:
    def __init__(self, min_num: int, max_num: int):
        self.min = min_num
        self.max = max_num

    def validate_value(self, value):
        if not isinstance(value, int):
            raise TypeError("Не верный тип данных")
        if value not in range(self.min, self.max + 1):
            raise ValueError(f"Оценка должна быть целым числом от {self.min} до {self.max}")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate_value(value)
        return setattr(instance, self.name, value)


class Student:
    name = Fio()

    def __init__(self, name: str, subjects_file: str):
        self.name = name
        self.file_name = subjects_file
        self.subjects = self.load_subject()

    def load_subject(self):
        """Загружает предметы из файла"""
        with open(self.file_name, 'r', newline='', encoding='UTF-8') as f:
            csv_file = csv.reader(f)
            subj = next(csv_file)
            subj_dict = {}
            for el in subj:
                subj_dict[el] = []
        return subj_dict

    def __str__(self):
        user = f'Студент: {self.name}'
        subject = f'Предметы: {self.file_name}'
        return user + '\n' + subject

    def add_grade(self, subject, grade):
        new_grade = Range(2, 5)
        new_grade = grade
        self.subjects[subject].append(new_grade)

    def add_test_score(self, param, param1):
        pass

    def get_average_grade(self):
        pass


if __name__ == '__main__':
    student = Student("Иван Иванов", "subjects.csv")

    student.add_grade("Математика", 6)
    print(student)
    # student.add_test_score("Математика", 85)
    #
    # student.add_grade("История", 5)
    # student.add_test_score("История", 92)
    #
    # average_grade = student.get_average_grade()
    # print(f"Средний балл: {average_grade}")
    #
    # average_test_score = student.get_average_test_score("Математика")
    # print(f"Средний результат по тестам по математике: {average_test_score}")

    print(student)
