import math

class Student:
    def init(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

    def input(self):
        self.id = input("Enter student ID: ")
        self.name = input("Enter student name: ")
        self.dob = input("Enter date of birth: ")

    def add_mark(self, course_id, mark):
        mark = math.floor(mark * 10) / 10
        self.marks[course_id] = mark

    def get_mark(self, course_id):
        if course_id in self.marks:
            return self.marks[course_id]
        return None

    def calculate_gpa(self, courses):
        marks = []
        credits = []
        for course in courses:
            mark = self.get_mark(course.get_id())
            if mark is not None:
                marks.append(mark)
                credits.append(course.get_credit())
        if len(marks) == 0:
            return None
        weighted_sum = sum(mark * credit for mark, credit in zip(marks, credits))
        total_credits = sum(credits)
        return weighted_sum / total_credits

    def list(self):
        print(
            "ID:", self.id,
            "| Name:", self.name,
            "| DoB:", self.dob
        )