
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
        self.id = input(
            "Enter student ID: "
        )
        self.name = input(
            "Enter student name: "
        )
        self.dob = input(
            "Enter date of birth: "
        )

    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark

    def get_mark(self, course_id):
        if course_id in self.marks:
            return self.marks[course_id]
        return None

    def list(self):
        print(
            "ID:",
            self.id,
            "| Name:",
            self.name,
            "| DoB:",
            self.dob
        )

class Course:
    def init(self, course_id, name):
        self.id = course_id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def input(self):
        self.id = input(
            "Enter course ID: "
        )
        self.name = input(
            "Enter course name: "
        )

    def list(self):
        print(
            "ID:",
            self.id,
            "| Name:",
            self.name
        )

class StudentMarkManagement:
    def init(self):
        self.students = []
        self.courses = []

    def input_students(self):
        number = int(
            input(
                "Enter number of students: "
            )
        )

        for i in range(number):
            print("\nStudent", i + 1)
            student = Student(
                "",
                "",
                ""
            )

            student.input()
            self.students.append(student)
        print(
            "\nStudents added successfully!"
        )

    def input_courses(self):
        number = int(
            input(
                "Enter number of courses: "
            )
        )

        for i in range(number):
            print("\nCourse", i + 1)
            course = Course(
                "",
                ""
            )
            course.input()
            self.courses.append(course)
        print(
            "\nCourses added successfully!"
        )

    def input_marks(self):
        if len(self.students) == 0:
            print(
                "There are no students!"
            )
            return

        if len(self.courses) == 0:
            print(
                "There are no courses!"
            )
            return
        print(
            "\n COURSES "
        )

        for i, course in enumerate(
            self.courses
        ):

            print(
                i + 1,
                ".",
                course.get_id(),
                "-",
                course.get_name()
            )

        choice = int(
            input(
                "Select a course: "
            )
        )

        if choice < 1 or choice > len(
            self.courses
        ):
            print(
                "Invalid course!"
            )
            return
        course = self.courses[
            choice - 1
        ]
        print(
            "\nEnter marks for:",
            course.get_name()
        )

        for student in self.students:
            mark = float(
                input(
                    "Enter mark for "
                    + student.get_name()
                    + ": "
                )
            )
            student.add_mark(
                course.get_id(),
                mark
            )
        print(
            "\nMarks added successfully!"
        )

    def list_students(self):
        if len(self.students) == 0:
            print(
                "There are no students!"
            )
            return
        print(
            "\n STUDENTS "
        )

        for student in self.students:
            student.list()
    
    def list_courses(self):
        if len(self.courses) == 0:
            print(
                "There are no courses!"
            )
            return

        print(
            "\n COURSES "
        )

        for course in self.courses:
            course.list()

    def show_marks(self):
        if len(self.students) == 0:
            print(
                "There are no students!"
            )
            return

        if len(self.courses) == 0:
            print(
                "There are no courses!"
            )
            return
        print(
            "\n COURSES "
        )

        for i, course in enumerate(
            self.courses
        ):
            print(
                i + 1,
                ".",
                course.get_id(),
                "-",
                course.get_name()
            )
        choice = int(
            input(
                "Select a course: "
            )
        )
        if choice < 1 or choice > len(
            self.courses
        ):
            print(
                "Invalid course!"
            )
            return
        course = self.courses[
            choice - 1
        ]
        
        print(
            "Course:",
            course.get_name()
        )

        for student in self.students:
            mark = student.get_mark(
                course.get_id()
            )
            if mark is not None:
                print(
                    student.get_name(),
                    "->",
                    mark
                )
            else:
                print(
                    student.get_name(),
                    "-> No mark"
                )
   
    def menu(self):
        while True:
            print(" STUDENT MARK MANAGEMENT")
            print("1. Input students")
            print("2. Input courses")
            print("3. Input marks")
            print("4. List students")
            print("5. List courses")
            print("6. Show student marks")
            print("0. Exit")

            choice = input( "Enter your choice: " )

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
            elif choice == "0":
                print("\nProgram finished.")
                break
            else:
                print(
                    "\nInvalid choice!"
                )
app = StudentMarkManagement()
app.menu()