import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from getpass import getpass
from controllers import AdminController, StudentController
from common import Utils


def university_system():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print('===== Welcome to the University Enrollment System =====')
        print('1. (A)dmin | 2. (S)tudent | 3. (X) Exit System')
        choice = input('Enter your choice (1-3 or first letters): ').lower()

        if choice in ['1', 'a']: 
            admin_controller = AdminController()
            admin_system(admin_controller)
            
        elif choice in ['2', 's']: 
            student_controller = StudentController()
            student_system(student_controller)

        elif choice in ['3', 'x']: exit()
        else: 
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Invalid option. Please try again.')


def admin_system(admin_controller):
    while True:
        print('\n<BACK|===== Admin System =====|')
        print('1. (C)lear all student data')
        print('2. (G)roup students by grade')
        print('3. (P)artition students by performance')
        print('4. (R)emove a student by ID')
        print('5. (S)how all registered students')
        print('6. (X) Logout and back to University System')

        choice = input('Enter your choice (1-6 or first letters): ').lower()
        if choice in ['1', 'c']: 
            admin_controller.clear_database()
            
        elif choice in ['2', 'g']: 
            admin_controller.group_students_by_grade()
            
        elif choice in ['3', 'p']: 
            admin_controller.partition_students_performance()
        
        elif choice in ['4', 'r']:
            student_id = input('Enter the student ID to remove: ')
            admin_controller.remove_student_by_id(student_id)
            
        elif choice in ['5', 's']: 
            admin_controller.show_registered_students()
        
        elif choice in ['6', 'x']:
            confirm = input('Are you sure you want to logout? (y/n): ').lower()
            if confirm in ['', 'y', 'yes']: 
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            
        else: print('Invalid option. Please try again.')
            

def student_system(student_controller):
    while True:
        print('\n<BACK|===== Student System =====|')
        print('1. (R)egister | 2. (L)ogin | 3. (X) Logout')
        choice = input('Enter your choice (1-3 or first letters): ').lower()

        if choice in ['1', 'r']:
            print('\nStudent Sign Up')
            name = input('Enter your name: ')
            email, password = Utils.get_credentials()
            
            if email and password:
                try: 
                    student = student_controller.register_student(name, email, password)
                    if student: print(f'Student {student.name} registered successfully with ID {student.student_id}.')
                except Exception as e: print(e)
       
        elif choice in ['2', 'l']:
            print('\nStudent Sign In')
            email, password = Utils.get_credentials()
            
            if email and password:
                try: 
                    student = student_controller.login_student(email, password)
                    if student:
                        print(f'Welcome {student.name}! You have successfully logged in.')
                        student_course_system(student_controller)
                except Exception as e: print(e)

        elif choice in ['3', 'x']: 
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else: print('Invalid option. Please try again.')


def student_course_system(student_controller):
    while True:
        print('\n<BACK|===== Student Course System =====|')
        print('1. (C)hange password')
        print('2. (E)nroll in a subject')
        print('3. (R)emove a subject')
        print('4. (S)how all enrolled subjects')
        print('5. (X) Logout and back to Student System')
        choice = input('Enter your choice (1-5 or first letters): ').lower()

        if choice in ['1', 'c']:
            old_password = getpass('Enter your old password: ')
            try:
                if student_controller.verify_password(old_password):
                    new_password = getpass('Enter your new password: ')
                    if not Utils.validate_password(new_password):
                        print('Password must start with UPPERCASE, followed by >= 5 letters and >= 3 digits.')
                    else: student_controller.change_student_password(old_password, new_password)
            except Exception as e: print(e)

        elif choice in ['2', 'e']:
            student_controller.enroll_random_subject()

        elif choice in ['3', 'r']:
            subject_id = input('Enter subject ID to remove: ')
            student_controller.remove_subject(subject_id)

        elif choice in ['4', 's']:
            student_controller.show_enrolled_subjects()

        elif choice in ['5', 'x']: 
            confirm = input('Are you sure you want to logout? (y/n):').lower() 
            if confirm in ['', 'y', 'yes']:
                os.system('cls' if os.name == 'nt' else 'clear')
                student_controller.logout_student()
                break
        else: print('Invalid option. Please try again.')


if __name__ == '__main__':
    university_system()