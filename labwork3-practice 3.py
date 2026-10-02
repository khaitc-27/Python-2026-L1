import math
import curses

class Student:
    def init(self, student_id="", name="", dob=""):
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
        return self.marks.get(course_id)

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
        total_credits = sum(credits)
        if total_credits == 0:
            return None
        weighted_sum = sum(mark * credit for mark, credit in zip(marks, credits))
        gpa = weighted_sum / total_credits
        return float(gpa)

    def list(self):
        print(
            "ID:", self.id,
            "| Name:", self.name,
            "| DoB:", self.dob
        )

class Course:
    def init(self, course_id="", name="", credit=0):
        self.id = course_id
        self.name = name
        self.credit = credit

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_credit(self):
        return self.credit

    def input(self):
        self.id = input("Enter course ID: ")
        self.name = input("Enter course name: ")
        self.credit = int(input("Enter credits: "))

    def list(self):
        print(
            "ID:", self.id,
            "| Name:", self.name,
            "| Credits:", self.credit
        )

class StudentMarkManagement:
    def init(self):
        self.students = []
        self.courses = []

    def input_students(self):
        number = int(input("Enter number of students: "))
        for i in range(number):
            print("\nStudent", i + 1)
            student = Student()
            student.input()
            if any(s.get_id() == student.get_id()
                   for s in self.students):
                print("Student ID already exists!")
                continue
            self.students.append(student)

        print("Students added successfully!")

    def input_courses(self):
        number = int(input("Enter number of courses: "))
        for i in range(number):
            print("\nCourse", i + 1)
            course = Course()
            course.input()
            if course.get_credit() <= 0:
                print("Credits must be positive!")
                continue
            if any(c.get_id() == course.get_id()
                   for c in self.courses):
                print("Course ID already exists!")
                continue
            self.courses.append(course)

        print("Courses added successfully!")

    def input_marks(self):
        if not self.students or not self.courses:
            print("Please input students and courses first!")
            return
        self.list_courses()
        choice = int(input("Select course number: "))
        if choice < 1 or choice > len(self.courses):
            print("Invalid course!")
            return
        course = self.courses[choice - 1]

        print("\nEnter marks for:", course.get_name())

        for student in self.students:
            mark = float(input(
                "Enter mark for " + student.get_name() + ": "
            ))
            if mark < 0 or mark > 10:
                print("Invalid mark! Must be between 0 and 10.")
                continue
            student.add_mark(course.get_id(), mark)

        print("Marks added successfully!")

    def list_students(self):
        print("\n STUDENTS ")
        for student in self.students:
            student.list()
    
    def list_courses(self):
        print("\n COURSES ")
        for i, course in enumerate(self.courses):
            print(i + 1, end=". ")
            course.list()

    def show_marks(self):
        if not self.courses:
            print("No courses available!")
            return
        self.list_courses()
        choice = int(input("Select course number: "))
        if choice < 1 or choice > len(self.courses):
            print("Invalid course!")
            return
        course = self.courses[choice - 1]

        print("\nCourse:", course.get_name())

        for student in self.students:
            mark = student.get_mark(course.get_id())
            if mark is not None:
                print(student.get_name(), "->", mark)
            else:
                print(student.get_name(), "-> No mark")
    
    def show_gpa(self):

        print("\n STUDENT GPA ")

        for student in self.students:
            gpa = student.calculate_gpa(self.courses)
            if gpa is None:
                print(student.get_name(), "-> No GPA")
            else:
                print(student.get_name(), "->", f"{gpa:.2f}")
    
    def sort_students_by_gpa(self):
        self.students.sort(
            key=lambda student:
                student.calculate_gpa(self.courses)
                if student.calculate_gpa(self.courses) is not None
                else -1,
            reverse=True
        )
        print("\n SORTED BY GPA ")
        self.show_gpa()

    def menu(self):
        while True:
            print(" STUDENT MARK MANAGEMENT - P3")
            print("1. Input students")
            print("2. Input courses")
            print("3. Input marks")
            print("4. List students")
            print("5. List courses")
            print("6. Show marks")
            print("7. Show GPA")
            print("8. Sort students by GPA")
            print("9. Curses UI")
            print("0. Exit")

            choice = input("Choose: ")

            if choice == "1":
                self.input_students()
            elif choice == "2":
                self.input_courses()
            elif choice == "3":
                self.input_marks()
            elif choice == "4":
                self.list_students()
            elif choice == "5":
                self.list_courses()
            elif choice == "6":
                self.show_marks()
            elif choice == "7":
                self.show_gpa()
            elif choice == "8":
                self.sort_students_by_gpa()
            elif choice == "9":
                curses.wrapper(self.curses_ui)
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")

    def curses_ui(self, stdscr):
        curses.curs_set(0)
        stdscr.clear()
        stdscr.addstr(
            1, 2,
            "STUDENT MARK MANAGEMENT",
            curses.A_BOLD
        )
        stdscr.addstr(
            3, 2,
            "STUDENTS AND GPA",
            curses.A_UNDERLINE
        )
        row = 5

        for student in self.students:
            gpa = student.calculate_gpa(self.courses)
            if gpa is None:
                gpa_text = "N/A"
            else:
                gpa_text = f"{gpa:.2f}"

            stdscr.addstr(
                row, 2,
                student.get_name() + " - GPA: " + gpa_text
            )
            row += 1

        stdscr.addstr(
            row + 2, 2,
            "Press any key to return..."
        )
        stdscr.refresh()
        stdscr.getch()

if __name__ == "__main__":
    app = StudentMarkManagement()
    app.menu()