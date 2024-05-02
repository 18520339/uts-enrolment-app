import os
import pickle
from typing import List
from common import Utils
from models import Student


class Database:
    def __init__(self, db_path: str = Utils.DATABASE_PATH):
        self._db_path = db_path
        self._students: List[Student] = []
        self._check_file_exists()
    
    @property
    def db_path(self):
        return self._db_path


    def _check_file_exists(self) -> None:
        # Checks if a file exists, creates it if not
        if not os.path.exists(self.db_path):
            with open(self.db_path, 'wb') as file:
                print(f'No data file found => Created new data file: {self.db_path}')
                pickle.dump([], file)


    def load_students(self) -> List[Student]:
        # Read and return the list of student objects from the data file
        self._check_file_exists()
        with open(self.db_path, 'rb') as file:
            return pickle.load(file)


    def get_student_if_existed(self, student_id_or_email: str) -> Student:
        # Check if a student record exists in the data file by student ID
        self._students = self.load_students()
        for student in self._students:
            if student_id_or_email in [student.student_id, student.email]:
                return student
        return None
    
    
    def create_student(self, student: Student) -> Student:
        # Create a new student record in the data file        
        self._students.append(student)
        with open(self.db_path, 'wb') as file:
            pickle.dump(self._students, file)
        return student

    
    def update_student(self, student: Student) -> None:
        # Write or update a student record in the data file
        current_student = self.get_student_if_existed(student.student_id)
        if current_student is None:
            raise ValueError(f'\t\tStudent {student.student_id} does not exist')
        
        self._students[self._students.index(current_student)] = student
        with open(self.db_path, 'wb') as file:
            pickle.dump(self._students, file)


    def remove_student_by_id(self, student: Student) -> None:
        # Removes a student record from the data file by student ID
        self._students.remove(student)
        with open(self.db_path, 'wb') as file:
            pickle.dump(self._students, file)

    
    def clear_database(self) -> None:
        # Clears all records from the data file
        with open(self.db_path, 'wb') as file:
            pickle.dump([], file)
            # print('All student records have been cleared.')