class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

    def calculate_average_grade(self):
        return sum(self.grade) / len(self.grade)

    def __str__(self):
        return f"Name:{self.name},Grades:{self.grades}"
