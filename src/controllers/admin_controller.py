from typing import Dict, List
from collections import defaultdict 
from models import Database
from common import Color, ScreenDisplayer


class AdminController:
    def __init__(self):
        self.database = Database()


    def clear_database(self) -> None:
        # Clear all student records from the database
        self.database.clear_database()
        print(Color.make_yellow('\tStudents data cleared.'))


    def group_students_by_grade(self) -> None:
        # Group students by their overall grade
        students = self.database.load_students()
        grade_groups: Dict[str, List[str]] = defaultdict(list)

        for student in students:
            grade_groups[student.overall_grade].append(student)

        if not grade_groups: 
            print(Color.make_yellow('\tGrade Grouping'))
            print('\t< Nothing to display >')
            return
        
        for grade, students in grade_groups.items():
            print(Color.make_yellow(f'\tGrade "{grade}" Group:'))
            ScreenDisplayer.display_students_table(students, {'subject_count': False, 'overall_grade': False})
            print()


    def partition_students_by_pass_fail(self) -> None:
        # Partition students into PASS and FAIL based on their average marks
        students = self.database.load_students()
        pass_students, fail_students = [], []

        for student in students:
            if student.average_mark >= 50 and student.overall_grade != 'Z':
                pass_students.append(student)
            else:
                fail_students.append(student)
        
        print(Color.make_yellow('\tPASSED Students:'))
        ScreenDisplayer.display_students_table(pass_students, {'subject_count': False})
        print()
        print(Color.make_yellow('\tFAILED Students:'))
        ScreenDisplayer.display_students_table(fail_students, {'subject_count': False})
        
        
    def remove_student_by_id(self, student_id: str) -> None:
        # Remove a student record from the database by student ID
        self.database.remove_student_by_id(student_id)
        print(Color.make_yellow(f'\tStudent with ID {student_id} has been removed.'))


    def show_registered_students(self) -> None:
        # Display the list of registered students
        print(Color.make_yellow('\tAll Registered Students:'))
        students = self.database.load_students()
        ScreenDisplayer.display_students_table(students, {'average_mark': False, 'overall_grade': False})