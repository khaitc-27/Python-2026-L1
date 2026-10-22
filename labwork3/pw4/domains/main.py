from domains.management import StudentMarkManagement

import input
import output

def menu():
    management = StudentMarkManagement()
    while True:
        print("STUDENT MARK MANAGEMENT")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List students")
        print("5. List courses")
        print("6. Show student marks")
        print("7. Show student GPA")
        print("8. Sort students by GPA")
        print("0. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            input.input_students(management)
        elif choice == "2":
            input.input_courses(management)
        elif choice == "3":
            input.input_marks(management)
        elif choice == "4":
            output.list_students(management)
        elif choice == "5":
            output.list_courses(management)
        elif choice == "6":
            output.show_marks(management)
        elif choice == "7":
            output.show_gpa(management)
        elif choice == "8":
            output.sort_students_by_gpa(management)
        elif choice == "0":
            print("\nProgram finished.")
            break
        else:
            print("\nInvalid choice!")
menu()