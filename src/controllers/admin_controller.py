from typing import Dict, List
from collections import defaultdict 
from models import Database
from common import Color


class AdminController:
    def __init__(self):
        self.database = Database()


    def clear_database(self) -> None:
        # Clear all student records from the database
        self.database.clear_database()


    def group_students_by_grade(self) -> None:
        # Group students by their overall grade
        print(Color.make_yellow('\tGrade Grouping'))
        students = self.database.load_students()
        grade_groups: Dict[str, List[str]] = defaultdict(list)

        for student in students:
            grade_groups[student.overall_grade].append(student.gpa_report())

        if not grade_groups: 
            print('\t\t< Nothing to display >')
            return
        
        for grade, reports in grade_groups.items():
            print(f"\t{grade:<2} --> [{', '.join(reports)}]")


    def partition_students_by_pass_fail(self) -> None:
        # Partition students into PASS and FAIL based on their average marks
        print(Color.make_yellow('\tPASS/FAIL Partition'))
        students = self.database.load_students()
        pass_students, fail_students = [], []

        for student in students:
            if student.average_mark >= 50 and student.overall_grade != 'Z':
                pass_students.append(student.gpa_report())
            else:
                fail_students.append(student.gpa_report())
        
        print(f"\tFAIL --> [{', '.join(fail_students)}]")
        print(f"\tPASS --> [{', '.join(pass_students)}]")
        
    
    def remove_student_by_id(self, student_id: str) -> None:
        # Remove a student record from the database by student ID
        current_student = self.database.get_student_if_existed(student_id)
        if current_student is None:
            print(Color.make_red(f'\tStudent {student_id} does not exist'))
            return
        
        print(Color.make_yellow(f'\tRemoving Student {student_id} Account'))
        self.database.remove_student(current_student)


    def show_registered_students(self) -> None:
        # Display the list of registered students
        print(Color.make_yellow('\tStudent List'))
        students = self.database.load_students()
        
        if not students:
            print('\t\t< Nothing to display >')
            return
        
        for student in students:
            print(f'\t{student.name} :: {student.student_id} --> Email: {student.email}')