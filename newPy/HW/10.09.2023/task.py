import csv
from typing import Dict

'''
Задание. Создайте класс студента.
- Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
- Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
- Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
- Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
'''


class NameValidator:
    def __set_name__(self, owner, name):
        self.field_name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.field_name]

    def __set__(self, instance, value):
        if not value.isalpha() or not value.istitle():
            raise ValueError(f"Invalid {self.field_name}: {value}")
        instance.__dict__[self.field_name] = value


class Subject:
    def __init__(self, name: str):
        self.name = name
        self.test_scores = []
        self.grades = []

    def add_test_score(self, score: int):
        if 0 <= score <= 100:
            self.test_scores.append(score)
        else:
            raise ValueError("Test score must be between 0 and 100")

    def add_grade(self, grade: int):
        if 2 <= grade <= 5:
            self.grades.append(grade)
        else:
            raise ValueError("Grade must be between 2 and 5")

    def average_test_score(self) -> float:
        if not self.test_scores:
            return 0
        return sum(self.test_scores) / len(self.test_scores)

    def average_grade(self) -> float:
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


class Student:
    first_name = NameValidator()
    last_name = NameValidator()

    def __init__(self, first_name: str, last_name: str, subjects_csv: str):
        self.first_name = first_name
        self.last_name = last_name
        self.subjects: Dict[str, Subject] = {}

        with open(subjects_csv, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                subject_name = row[0]
                self.subjects[subject_name] = Subject(subject_name)

    def add_test_score(self, subject_name: str, score: int):
        if subject_name not in self.subjects:
            raise ValueError(f"Invalid subject: {subject_name}")
        self.subjects[subject_name].add_test_score(score)

    def add_grade(self, subject_name: str, grade: int):
        if subject_name not in self.subjects:
            raise ValueError(f"Invalid subject: {subject_name}")
        self.subjects[subject_name].add_grade(grade)

    def average_test_scores(self) -> Dict[str, float]:
        return {subject_name: self.subjects[subject_name].average_test_score() for subject_name in self.subjects}

    def average_grades(self) -> Dict[str, float]:
        return {subject_name: self.subjects[subject_name].average_grade() for subject_name in self.subjects}


if __name__ == '__main__':
    student = Student("Иван", "Иванов", "subjects.csv")
    student.add_test_score("Math", 90)
    student.add_test_score("English", 80)
    student.add_grade("Math", 5)
    student.add_grade("English", 4)

    print("Средний балл по тестам:")
    for subject, average_score in student.average_test_scores().items():
        print(f"{subject}: {average_score:.2f}")

    print("\nСредний балл по оценкам:")
    for subject, average_grade in student.average_grades().items():
        print(f"{subject}: {average_grade:.2f}")
