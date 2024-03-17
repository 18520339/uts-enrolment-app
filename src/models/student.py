from typing import List
from models import Subject
from common.helper import Utils


class Student:
    def __init__(self, name: str, email: str, password: str):
        self._student_id = Utils.generate_student_id()
        self._name = name
        self._email = email
        self._password = password
        self._subjects: List[Subject] = []
        self._average_mark = 0
        self._overall_grade = None # Grade will be calculated based on the mark

    @property
    def student_id(self):
        return self._student_id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

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


    def _recalculate_academic_performance(self):
        # Recalculates the student's average mark and overall grade based on the subjects enrolled.
        self._average_mark = sum(subject.mark for subject in self.subjects) / len(self.subjects)
        self._overall_grade = Utils.calculate_grade(self._average_mark)
        print(f'Academic performance recalculated. Average mark: {self._average_mark}, Grade: {self._overall_grade}')


    def change_password(self, old_password: str, new_password: str) -> None:
        # Changes the student's password after validating the new password.
        if old_password != self.password:
            print('Invalid current password. Password change failed.')
            return
        
        if not Utils.validate_password(new_password):
            print('Password change failed. Make sure your new password format is valid.')
            return

        self.password = new_password
        print('Password changed successfully.')


    def enroll_subject(self, subject: Subject) -> None:
        # Enrolls the student in a subject if not already enrolled
        if subject not in self.subjects:
            self.subjects.append(subject)
            print(f'Enrolled in subject {subject.subject_id} with mark {subject.mark} and grade {subject.grade}.')
            self._recalculate_academic_performance()
        else:
            print('You have already enrolled in this subject.')

  
    def remove_subject(self, subject_id: str) -> None:
        # Removes a subject from the student's enrolled subjects list by subject ID.
        for subject in self.subjects:
            if subject.subject_id == subject_id:
                self.subjects.remove(subject)
                print(f'Subject {subject_id} removed successfully.')
                self._recalculate_academic_performance()
        print('Subject not found.')


    def show_enrolled_subjects(self):
        if len(self.subjects) == 0:
            print('No subjects enrolled.')
            return

        for subject in self.subjects:
            print(f'Subject ID: {subject.subject_id}, Mark: {subject.mark}, Grade: {subject.grade}')