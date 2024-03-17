import os
import pickle
from typing import List
from models import Student


class Database:
    def __init__(self, file_name: str = 'students.data'):
        self._file_name = file_name
        self._check_file_exists()
    
    @property
    def file_name(self):
        return self._file_name

    def _check_file_exists(self) -> None:
        # Checks if a file exists, creates it if not
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'wb') as file:
                pickle.dump([], file)
                print(f'No data file found => Created new data file: {self.file_name}')

    def load_students(self) -> List[Student]:
        # Read and return the list of student objects from the data file
        self._check_file_exists()
        with open(self.file_name, 'rb') as file:
            return pickle.load(file)

    def write_student(self, student: Student) -> None:
        # Write or update a student record in the data file
        students = self.load_students()
        for i, existing_student in enumerate(students):
            if existing_student.student_id == student.student_id:
                students[i] = student
                break
        else: students.append(student)

        with open(self.filename, 'wb') as file:
            pickle.dump(students, file)

    def remove_student(self, student_id: str) -> None:
        # Removes a student record from the data file by student ID
        students = self.load_students()
        students = [student for student in students if student.student_id != student_id]
        with open(self.filename, 'wb') as file:
            pickle.dump(students, file)
    
    def clear_data(self) -> None:
        # Clears all records from the data file
        with open(self.filename, 'wb') as file:
            pickle.dump([], file)
            print('All student records have been cleared.')