from typing import List
from models import Subject
from common import Randomizer


class Student:
    def __init__(self, name: str, email: str, password: str):
        self._student_id = Randomizer.generate_student_id()
        self._name = name
        self._email = email.lower()
        self._password = password
        self._subjects: List[Subject] = []
        self._average_mark = 25 # Default GPA if students haven't enrolled any subjects
        self._overall_grade = 'Z' # Grade will be calculated based on the mark

    @property # This creates an API that does not allow a value to be set
    def student_id(self):
        return self._student_id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email.lower()

    @property
    def password(self):
        return self._password

    @property
    def subjects(self):
        return self._subjects

    @property
    def average_mark(self):
        return self._average_mark

    @property
    def overall_grade(self):
        return self._overall_grade
    
    @password.setter
    def password(self, new_password: str):
        self._password = new_password


    def _recalculate_gpa(self) -> None:
        # Recalculates the student's average mark and overall grade based on the subjects enrolled.
        self._average_mark = sum(subject.mark for subject in self.subjects) / len(self.subjects) if self.subjects else 0
        self._overall_grade = Subject.calculate_grade(self._average_mark)


    def enroll_subject(self, subject: Subject) -> bool:
        # Enrolls the student in a subject if not already enrolled
        if subject not in self.subjects:
            self.subjects.append(subject)
            self._recalculate_gpa()
            return True
        return False

  
    def remove_subject_by_id(self, subject_id: str) -> bool:
        # Removes a subject from the student's enrolled subjects list by subject ID.
        for subject in self.subjects:
            if subject.subject_id == subject_id:
                self.subjects.remove(subject)
                self._recalculate_gpa()
                return True
        return False


    def show_enrolled_subjects(self) -> None:
        if len(self.subjects) == 0: return
        for subject in self.subjects: print(f'\t\t{subject}')
        
        
    def gpa_report(self) -> None:
        return f'{self.name} :: {self.student_id} --> GRADE: {self.overall_grade:>2} - MARK: {self.average_mark:05.2f}'