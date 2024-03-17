from typing import Dict, List
from collections import defaultdict 
from models import Database, Student
from common.helper import Utils


class AdminController:
    def __init__(self):
        self.database = Database()


    def clear_database(self) -> None:
        # Clears all student records from the database
        self.database.clear_data()
        print("Database cleared successfully.")


    def group_student_by_grade(self) -> None:
        # Groups students by their overall grade
        students = self.database.load_students()
        grade_groups: Dict[str, List[Student]] = defaultdict(list)

        for student in students:
            grade_groups[student.overall_grade].append(student)

        for grade, students in grade_groups.items():
            print(f'Grade {grade}:')
            Utils.display_students_table(students, {'email': False, 'overall_grade': False})


    def remove_student_by_id(self, student_id: str) -> None:
        # Removes a student record from the database by student ID
        if self.database.remove_student(student_id):
            print(f'Student with ID {student_id} has been removed.')
        else:
            print(f'No student found with ID {student_id}.')


    def partition_students(self) -> None:
        # Partitions students into PASS and FAIL based on their average marks
        students = self.database.load_students()
        pass_students, fail_students = [], []

        for student in students:
            if student.average_mark >= 50:
                pass_students.append(student)
            else:
                fail_students.append(student)
        
        print('PASSED Students:')
        Utils.display_students_table(pass_students)

        print('FAILED Students:')
        Utils.display_students_table(pass_students)


    def show_registered_students(self) -> None:
        # Lists all registered students
        students = self.database.load_students()
        if not students:
            print("No students are currently registered.")
            return
        Utils.display_students_table(students, {'average_mark': False, 'overall_grade': False})