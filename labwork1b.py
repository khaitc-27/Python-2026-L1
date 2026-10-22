students = []
courses = []
marks = {}

def input_students():
    number = int(
        input("Enter number of students: ")
    )
    for i in range(number):
        print("\nStudent", i + 1)
        student_id = input(
            "Enter student ID: "
        )
        name = input(
            "Enter student name: "
        )
        dob = input(
            "Enter date of birth: "
        )
        student = {
            "id": student_id,
            "name": name,
            "dob": dob
        }
        students.append(student)
    print("\nStudents added successfully!")

def input_courses():
    number = int(
        input("Enter number of courses: ")
    )
    for i in range(number):
        print("\nCourse", i + 1)
        course_id = input(
            "Enter course ID: "
        )
        name = input(
            "Enter course name: "
        )
        course = {
            "id": course_id,
            "name": name
        }
        courses.append(course)
    print("\nCourses added successfully!")

def input_marks():
    if len(students) == 0:
        print("There are no students!")
        return
    if len(courses) == 0:
        print("There are no courses!")
        return
    print("\n COURSES ")

    for i, course in enumerate(courses):
        print(
            i + 1,
            ".",
            course["id"],
            "-",
            course["name"]
        )
    choice = int(
        input("Select a course: ")
    )
    if choice < 1 or choice > len(courses):
        print("Invalid course!")
        return
    
    course = courses[choice - 1]
    course_id = course["id"]
    marks[course_id] = {}
    print(
        "\nEnter marks for:",
        course["name"]
    )

    for student in students:
        mark = float(
            input(
                "Enter mark for "
                + student["name"]
                + ": "
            )
        )
        marks[course_id][student["id"]] = mark
    print("\nMarks added successfully!")

def list_students():
    if len(students) == 0:
        print("There are no students!")
        return
    print("\n STUDENTS ")

    for student in students:
        print(
            "ID:",
            student["id"],
            "| Name:",
            student["name"],
            "| DoB:",
            student["dob"]
        )

def list_courses():
    if len(courses) == 0:
        print("There are no courses!")
        return
    print("\n COURSES ")

    for course in courses:
        print(
            "ID:",
            course["id"],
            "| Name:",
            course["name"]
        )

def show_marks():
    if len(students) == 0:
        print("There are no students!")
        return
    if len(courses) == 0:
        print("There are no courses!")
        return
    print("\n COURSES ")

    for i, course in enumerate(courses):
        print(
            i + 1,
            ".",
            course["id"],
            "-",
            course["name"]
        )

    choice = int(
        input("Select a course: ")
    )
    if choice < 1 or choice > len(courses):
        print("Invalid course!")
        return
    
    course = courses[choice - 1]
    course_id = course["id"]
    
    print(
        "Course:",
        course["name"]
    )
    
    if course_id not in marks:
        print("No marks entered!")
        return

    for student in students:
        student_id = student["id"]
        if student_id in marks[course_id]:
            print(
                student["name"],
                "->",
                marks[course_id][student_id]
            )
        else:
            print(
                student["name"],
                "-> No mark"
            )

def menu():
    while True:
        print("STUDENT MARK MANAGEMENT")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List students")
        print("5. List courses")
        print("6. Show student marks")
        print("0. Exit")
        
        choice = input(
            "Enter your choice: "
        )

        if choice == "1":
            input_students()
        elif choice == "2":
            input_courses()
        elif choice == "3":
            input_marks()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            show_marks()
        elif choice == "0":
            print("\nProgram finished.")
            break
        else:
            print("\nInvalid choice!")

menu()