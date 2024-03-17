import os
import pickle
from typing import List
from common import Utils
from models import Student

class Database:
    def __init__(self, db_path: str = Utils.DATABASE_PATH):
        self._db_path = db_path
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


    def write_student(self, student: Student) -> None:
        # Write or update a student record in the data file
        students = self.load_students()
        for i, existing_student in enumerate(students):
            if existing_student.student_id == student.student_id:
                students[i] = student
                break
        else: students.append(student)

        with open(self.db_path, 'wb') as file:
            pickle.dump(students, file)


    def remove_student(self, student_id: str) -> bool:
        # Removes a student record from the data file by student ID
        students = self.load_students()
        for student in students:
            if student.student_id == student_id:
                students.remove(student)
                with open(self.db_path, 'wb') as file:
                    pickle.dump(students, file)
                return True
        return False

    
    def clear_data(self) -> None:
        # Clears all records from the data file
        with open(self.db_path, 'wb') as file:
            pickle.dump([], file)
            print('All student records have been cleared.')