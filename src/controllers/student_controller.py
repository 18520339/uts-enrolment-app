from models import Student, Subject, Database
from common import Color


class StudentController:
    def __init__(self):
        self.database = Database()
        self.current_student = None # The logged-in student


    def register_student(self, email: str, password: str) -> Student:
        # Register a new student if the email doesn't already exist
        if self.current_student is not None:
            raise Exception('\tAnother student is already logged in. Please logout first')
        
        # Check if the student already exists
        student = self.database.get_student_if_existed(email)
        if student is not None:
            raise Exception(f'\tStudent {student.name} already exists')
        
        # Create and save the new student
        student = Student(input('\tName: '), email, password)
        return self.database.create_student(student)


    def login_student(self, email: str, password: str) -> Student:
        # Verify a student's login credentials. Returns the Student object if successful, else None
        if self.current_student is not None:
            raise Exception('\tAnother student is already logged in. Please logout first')
        
        student = self.database.get_student_if_existed(email)
        if student is not None and student.password == password:
            self.current_student = student
            return student
        raise Exception('\tStudent does not exist')

    
    def change_student_password(self, new_password: str) -> None:
        # Change the password for the current logged-in student
        if self.current_student is None:
            raise Exception('\t\tNo student is logged in')
                
        self.current_student.password = new_password
        self.database.update_student(self.current_student)


    def enroll_subject(self) -> None:
        # Enroll the student in a subject with random ID, if not already enrolled and if enrollment limit not reached 
        # This is a simplified version without subject ID checking, assuming subject creation here for demonstration
        if self.current_student is None:
            raise Exception('\t\tNo student is logged in')
        
        if len(self.current_student.subjects) < 4:
            new_subject = Subject()
            print(Color.make_yellow(f'\t\tEnrolling in Subject-{new_subject.subject_id}'))
            
            if self.current_student.enroll_subject(new_subject):
                self.database.update_student(self.current_student)
                print(Color.make_yellow(f'\t\tYou are now enrolled in {len(self.current_student.subjects)} out of 4 subjects'))
            else: print(Color.make_red('\t\tYou have already enrolled in this subject.'))
        else: print(Color.make_red('\t\tStudents are allowed to enrol in 4 subjects only'))


    def remove_subject_by_id(self, subject_id: str) -> None:
        # Remove a subject from the current student's enrollment
        if self.current_student is None:
            raise Exception('\t\tNo student is logged in')

        if len(self.current_student.subjects) >= 0:
            print(Color.make_yellow(f'\t\tDropping Subject-{subject_id}'))
            
            if self.current_student.remove_subject_by_id(subject_id):
                self.database.update_student(self.current_student)
                print(Color.make_yellow(f'\t\tYou are now enrolled in {len(self.current_student.subjects)} out of 4 subjects'))
            else: print(Color.make_red('\t\tSubject not found in your enrollment'))
        else: print(Color.make_red('\t\tYou are not enrolled in any subjects'))


    def show_enrolled_subjects(self) -> None:
        # Show the subjects the current student is enrolled in
        if self.current_student is None:
            raise Exception('\t\tNo student is logged in')
        
        print(Color.make_yellow(f'\t\tShowing {len(self.current_student.subjects)} subjects'))
        self.current_student.show_enrolled_subjects()

    
    def logout_student(self) -> None:
        # Log out the current student
        if self.current_student is None:
            raise Exception('\t\tNo student is logged in')
        self.current_student = None