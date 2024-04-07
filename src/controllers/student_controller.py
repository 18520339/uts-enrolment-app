from models import Student, Subject, Database
from common import Randomizer, PasswordSecurer


class StudentController:
    def __init__(self):
        self.database = Database()
        self.current_student = None # The logged-in student


    def register_student(self, name: str, email: str, password: str) -> Student:
        # Register a new student if the email doesn't already exist
        if self.current_student is not None:
            raise Exception('Another student is already logged in. Please logout first.')
        
        # Check if email already exists
        students = self.database.load_students()
        if any(student.email == email for student in students):
            raise ValueError('A student with this email already exists.')
        
        # Create and save the new student
        hashed_password = PasswordSecurer.hash_password(password)
        new_student = Student(name, email, hashed_password)
        self.database.write_student(new_student)
        return new_student


    def login_student(self, email: str, password: str) -> Student:
        # Validate a student's login credentials. Returns the Student object if successful, else None
        if self.current_student is not None:
            raise Exception('Another student is already logged in. Please logout first.')
        
        students = self.database.load_students()
        for student in students:
            if student.email == email and PasswordSecurer.verify_password(student.password, password):
                self.current_student = student
                return student
        raise Exception("Login failed. Check your email and password or register if you haven't.")

    
    def change_student_password(self, new_password: str) -> None:
        # Change the password for the current logged-in student
        if self.current_student is None:
            raise Exception('No student is logged in.')
                
        self.current_student.password = PasswordSecurer.hash_password(new_password)
        self.database.write_student(self.current_student)
        print('Password changed successfully.')


    def enroll_random_subject(self) -> None:
        # Enroll the student in a subject by subject ID, if not already enrolled and if enrollment limit not reached 
        # This is a simplified version without subject ID checking, assuming subject creation here for demonstration
        if self.current_student is None:
            raise Exception('No student is logged in.')
        
        if len(self.current_student.subjects) < 4:
            random_subject = Subject(
                name = Randomizer.generate_subject_name(),
                mark = Randomizer.generate_subject_mark() 
            )
            if self.current_student.enroll_subject(random_subject):
                self.database.write_student(self.current_student)
                print(f'You are now enrolled in {len(self.current_student.subjects)}/4 subjects.')
            else: print('You have already enrolled in this subject.')
        else: print('Students are allowed to enroll 4 subjects only.')


    def remove_subject(self, subject_id: str) -> None:
        # Remove a subject from the current student's enrollment
        if self.current_student is None:
            raise Exception('No student is logged in.')

        if len(self.current_student.subjects) >= 0:
            if self.current_student.remove_subject(subject_id):
                self.database.write_student(self.current_student)
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