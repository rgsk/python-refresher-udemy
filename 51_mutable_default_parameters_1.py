from typing import List, Optional


class Student():
    # This is bad!
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        self.name = name
        self.grades = grades or []

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def take_exam(self, result: int):
        self.grades.append(result)


mehak = Student('Mehak')
mehak.take_exam(100)
print(mehak.grades)
rolf = Student('Rolf')
print(rolf.grades)
