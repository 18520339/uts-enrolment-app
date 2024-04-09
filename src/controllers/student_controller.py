from models import Student, Subject, Database
from common import PasswordSecurer


class StudentController:
    def __init__(self):
        self.database = Database()
        self.current_student = None # The logged-in student


    def register_student(self, name: str, email: str, password: str) -> Student:
        # Register a new student if the email doesn't already exist
        if self.current_student is not None:
            raise Exception('Another student is already logged in. Please logout first.')
        
        # Create and save the new student
        hashed_password = PasswordSecurer.hash_password(password)
        new_student = Student(name, email, hashed_password)
        return self.database.create_student(new_student)


    def login_student(self, email: str, password: str) -> Student:
        # Verify a student's login credentials. Returns the Student object if successful, else None
        if self.current_student is not None:
            raise Exception('Another student is already logged in. Please logout first.')
        
        student = self.database.get_student_if_existed(email)
        if student is not None and PasswordSecurer.verify_password(student.password, password):
            self.current_student = student
            return student
        raise Exception("Login failed. Check your email and password or register if you haven't.")

    
    def change_student_password(self, new_password: str) -> None:
        # Change the password for the current logged-in student
        if self.current_student is None:
            raise Exception('No student is logged in.')
                
        self.current_student.password = PasswordSecurer.hash_password(new_password)
        self.database.update_student(self.current_student)
        print('Password changed successfully.')


    def enroll_subject(self) -> None:
        # Enroll the student in a subject with random ID, if not already enrolled and if enrollment limit not reached 
        # This is a simplified version without subject ID checking, assuming subject creation here for demonstration
        if self.current_student is None:
            raise Exception('No student is logged in.')
        
        if len(self.current_student.subjects) < 4:
            if self.current_student.enroll_subject(Subject()):
                self.database.update_student(self.current_student)
                print(f'You are now enrolled in {len(self.current_student.subjects)}/4 subjects.')
            else: print('You have already enrolled in this subject.')
        else: print('Students are allowed to enroll 4 subjects only.')


    def remove_subject_by_id(self, subject_id: str) -> None:
        # Remove a subject from the current student's enrollment
        if self.current_student is None:
            raise Exception('No student is logged in.')

        if len(self.current_student.subjects) >= 0:
            if self.current_student.remove_subject_by_id(subject_id):
                self.database.update_student(self.current_student)
                print(f'You are now enrolled in {len(self.current_student.subjects)}/4 subjects.')
            else: print('Subject not found in your enrollment.')
        else: print('You are not enrolled in any subjects.')


    def show_enrolled_subjects(self) -> None:
        # Show the subjects the current student is enrolled in
        if self.current_student is None:
            raise Exception('No student is logged in.')
        self.current_student.show_enrolled_subjects()

    
    def logout_student(self) -> None:
        # Log out the current student
        if self.current_student is None:
            raise Exception('No student is logged in.')
        self.current_student = None
        print('You have been logged out successfully.')