def input_students(management):
    management.input_students()

def input_courses(management):
    management.input_courses()

def input_marks(management):
    management.input_marks()

def save_students(management):
    with open(
        "students.txt",
        "w",
        encoding="utf-8"
    ) as file:
        for student in management.students:
            file.write(
                student.get_id()
                + "|"
                + student.get_name()
                + "|"
                + student.get_dob()
                + "\n"
            )
    print("Students saved successfully!")

def save_courses(management):
    with open(
        "courses.txt",
        "w",
        encoding="utf-8"
    ) as file:
        for course in management.courses:
            file.write(
                course.get_id()
                + "|"
                + course.get_name()
                + "|"
                + str(course.get_credit())
                + "\n"
            )
    print("Courses saved successfully!")

def save_marks(management):
    with open(
        "marks.txt",
        "w",
        encoding="utf-8"
    ) as file:
        for student in management.students:
            marks = student.get_all_marks()
            for course_id, mark in marks.items():
                file.write(
                    student.get_id()
                    + "|"
                    + course_id
                    + "|"
                    + str(mark)
                    + "\n"
                )
    print("Marks saved successfully!")