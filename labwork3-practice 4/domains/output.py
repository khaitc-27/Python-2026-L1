def list_students(management):
    if len(management.students) == 0:
        print("There are no students!")
        return

    print("\n STUDENTS ")

    for student in management.students:
        student.list()

def list_courses(management):
    if len(management.courses) == 0:
        print("There are no courses!")
        return

    print("\n COURSES ")

    for course in management.courses:
        course.list()

def show_marks(management):
    if len(management.students) == 0:
        print("There are no students!")
        return
    if len(management.courses) == 0:
        print("There are no courses!")
        return

    print("\n COURSES ")

    for i, course in enumerate(management.courses):
        print(
            i + 1,
            ".",
            course.get_id(),
            "-",
            course.get_name()
        )

    choice = int(input("Select a course: "))

    if choice < 1 or choice > len(management.courses):
        print("Invalid course!")
        return

    course = management.courses[choice - 1]

    print("Course:", course.get_name())

    for student in management.students:
        mark = student.get_mark(course.get_id())
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

def show_gpa(management):
    if len(management.students) == 0:
        print("There are no students!")
        return

    print("\n STUDENT GPA ")

    for student in management.students:
        gpa = student.calculate_gpa(
            management.courses
        )
        if gpa is None:
            print(
                student.get_name(),
                "-> No GPA"
            )
        else:
            print(
                student.get_name(),
                "-> GPA:",
                round(gpa, 2)
            )

def sort_students_by_gpa(management):
    def get_gpa(student):
        gpa = student.calculate_gpa(
            management.courses
        )
        if gpa is None:
            return -1
        return gpa

    management.students.sort(
        key=get_gpa,
        reverse=True
    )

    print(
        "\n STUDENTS SORTED BY GPA "
    )

    for student in management.students:
        gpa = student.calculate_gpa(
            management.courses
        )
        if gpa is None:
            print(
                student.get_name(),
                "-> No GPA"
            )
        else:
            print(
                student.get_name(),
                "-> GPA:",
                round(gpa, 2)
            )