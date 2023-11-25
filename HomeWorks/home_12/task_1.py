import csv


class Fio:

    @classmethod
    def validate_text(cls, value):
        if not isinstance(value, str):
            raise TypeError("Тип данных не строка")
        lst = value.split()
        for el in lst:
            if not el.isalpha() or not el.istitle():
                raise ValueError(
                    'ФИО должно состоять только из букв и начинаться с заглавной буквы')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate_text(value)
        return setattr(instance, self.name, value)


class Student:
    name = Fio()

    def __init__(self, name: str, subjects_file: str):
        self.name = name
        self.file_name = subjects_file
        self.subjects = self.load_subject()
        self.subjects_grade = {}
        self.subjects_test_score = {}

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
        subjects = []
        for key in self.subjects_grade.keys():
            if key not in subjects:
                subjects.append(key)
        for key in self.subjects_test_score.keys():
            if key not in subjects:
                subjects.append(key)
        subjects = f'Предметы: {", ".join(subjects)}'
        return user + '\n' + subjects

    def add_grade(self, subject: str, grade: int):
        """
        Добавление отметки по предмету
        :param subject: предмет
        :param grade: отметка
        :return:
        """
        if grade not in range(2, 6):
            raise ValueError("Оценка должна быть целым числом от 2 до 5")
        if subject not in self.subjects:
            raise ValueError(f'Предмет {subject} не найден')
        if subject not in self.subjects_grade:
            self.subjects_grade[subject] = []
        self.subjects_grade[subject].append(grade)

    def add_test_score(self, subject: str, score: int):
        """
        Добавляет тестовые баллы по предмету
        :param subject: предмет
        :param score: баллы
        :return:
        """
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        if score not in range(0, 101):
            raise ValueError("Результат теста должен быть целым числом от 0 до 100")
        if subject not in self.subjects_test_score:
            self.subjects_test_score[subject] = []
        self.subjects_test_score[subject].append(score)

    def get_average_grade(self):
        count = 0
        summa_all_grade = 0
        for key, item in self.subjects_grade.items():
            count += len(item)
            summa_all_grade += sum(item)
        return summa_all_grade / count

    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        return sum(self.subjects_test_score[subject]) / len(
            self.subjects_test_score[subject])


if __name__ == '__main__':
    student = Student("Иван Иванов", "subjects.csv")

    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)

    # student.add_grade("Биология", 5)
    # student.add_test_score("Биология", 92)

    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("Биология")
    print(f"Средний результат по тестам по математике: {average_test_score}")

    print(student)
