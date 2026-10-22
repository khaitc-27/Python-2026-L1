from domains.student import Student
from domains.course import Course

class StudentMarkManagement:
    def init(self):
        self.students = []
        self.courses = []

    def add_student(self):
        student = Student("", "", "")
        student.input()
        self.students.append(student)

    def add_course(self):
        course = Course("", "", 0)
        course.input()
        self.courses.append(course)

    def input_students(self):
        number = int(input("Enter number of students: "))
        for i in range(number):
            print("\nStudent", i + 1)
            self.add_student()
        print("\nStudents added successfully!")

    def input_courses(self):
        number = int(input("Enter number of courses: "))
        for i in range(number):
            print("\nCourse", i + 1)
            self.add_course()
        print("\nCourses added successfully!")

    def input_marks(self):
        if len(self.students) == 0:
            print("There are no students!")
            return
        if len(self.courses) == 0:
            print("There are no courses!")
            return
        print("\n  COURSES ")

        for i, course in enumerate(self.courses):
            print(
                i + 1,
                ".",
                course.get_id(),
                "-",
                course.get_name()
            )
        choice = int(input("Select a course: "))

        if choice < 1 or choice > len(self.courses):
            print("Invalid course!")
            return

        course = self.courses[choice - 1]
        print("\nEnter marks for:", course.get_name())

        for student in self.students:
            mark = float(
                input(
                    "Enter mark for "
                    + student.get_name()
                    + ": "
                )
            )

            if mark < 0 or mark > 10:
                print("Mark must be between 0 and 10!")
                continue

            student.add_mark(
                course.get_id(),
                mark
            )
        print("\nMarks added successfully!")