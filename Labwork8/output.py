from __future__ import annotations
from typing import Protocol


class CourseMarks(Protocol):
    course_id: str
    attendance: str | int
    midterm: str | int
    final: str | int
    gpa: str | float


class Student(Protocol):
    name: str
    id: str
    dob: str
    courses_marks: list[CourseMarks]
    gpa: str | float


class BasicInfo(Protocol):
    id: str
    name: str


def format_str(content: str, width: int) -> str:
    """Format string to fit in a table cell."""
    return f"| {content}{' '*(width-len(content))} "

def print_table(students: list[Student], courses: list[BasicInfo]) -> None:
    data_column_content = ["Data", "ID", "DOB"]
    data_column_content.extend([f"Course: {course.name}" for course in courses])
    data_column_width = max([len(content) for content in data_column_content])
    del data_column_content

    width_for_each_student_column: list[int] = []
    for student in students:
        student_column_content = [student.name, student.id, student.dob]
        for course_marks in student.courses_marks:
            attendance, midterm, final, gpa = (
                course_marks.attendance,
                course_marks.midterm,
                course_marks.final,
                course_marks.gpa,
            )
            string_to_print = f"{attendance} {midterm} {final} {gpa}"
            student_column_content.append(string_to_print)
        student_column_content.append(str(student.gpa))
        width_for_each_student_column.append(max([len(content) for content in student_column_content]))

    
    print(format_str(content="Data", width=data_column_width), end="")
    for i, student in enumerate(students):
        print(format_str(content=student.name, width=width_for_each_student_column[i]), end="")
    print()

    
    print("=" * (data_column_width + 3), end="")
    for width in width_for_each_student_column:
        print("=" * (width + 3), end="")
    print()

    print(format_str(content="ID", width=data_column_width), end="")
    for i, student in enumerate(students):
        print(format_str(content=student.id, width=width_for_each_student_column[i]), end="")
    print()

    print(format_str(content="DOB", width=data_column_width), end="")
    for i, student in enumerate(students):
        print(format_str(content=student.dob, width=width_for_each_student_column[i]), end="")
    print()

    for course in courses:
        print(format_str(content=f"Course: {course.name}", width=data_column_width), end="")
        for i, student in enumerate(students):
            for course_marks in student.courses_marks:
                if course_marks.course_id == course.id:
                    attendance, midterm, final, gpa = (
                        course_marks.attendance,
                        course_marks.midterm,
                        course_marks.final,
                        course_marks.gpa,
                    )
                    string_to_print = f"{attendance} {midterm} {final} {gpa}"
                    print(format_str(content=string_to_print, width=width_for_each_student_column[i]), end="")
                    break
            else:
                print(format_str(content="", width=width_for_each_student_column[i]), end="")
        print()

    print(format_str(content="GPA", width=data_column_width), end="")
    for i, student in enumerate(students):
        print(format_str(content=str(student.gpa), width=width_for_each_student_column[i]), end="")
    print()
