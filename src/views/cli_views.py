import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from getpass import getpass
from controllers import AdminController, StudentController
from common import Validator, PasswordSecurer, Color


def university_system():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        choice = input(Color.make_cyan(
            '===== Welcome to the University Enrollment System ====='
            '\n1. (A)dmin | 2. (S)tudent | 3. (X) Exit'
            '\n👉 Enter your choice (1-3 or first letters): '
        )).strip().upper()

        if choice in ['1', 'A']: admin_system(AdminController())
        elif choice in ['2', 'S']: student_system(StudentController())
        elif choice in ['3', 'X']: 
            print(Color.make_yellow('Thank You'))
            exit()
        else: print(Color.make_red('Invalid option. Please try again.'))


def admin_system(admin_controller):
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        choice = input(Color.make_cyan(
            '\n<BACK|===== Admin System =====|'
            '\n1. (C)lear all student data'
            '\n2. (G)roup students by grade'
            '\n3. (P)artition students by performance'
            '\n4. (R)emove a student by ID'
            '\n5. (S)how all registered students'
            '\n6. (X) Logout and back to University System'
            '\n👉 Enter your choice (1-6 or first letters): '
        )).strip().lower()
        
        try: 
            if choice in ['1', 'c']: 
                confirm = input(Color.make_red('\tAre you sure want to clear the database (Y)ES/(N)O: ')).strip().upper()
                if confirm in ['Y', 'YES']: admin_controller.clear_database()
                
            elif choice in ['2', 'g']: admin_controller.group_students_by_grade()
            elif choice in ['3', 'p']: admin_controller.partition_students_by_pass_fail()
            elif choice in ['4', 'r']: admin_controller.remove_student_by_id(input('\tStudent ID to remove: ').strip())
            elif choice in ['5', 's']: admin_controller.show_registered_students()
            elif choice in ['6', 'x']: 
                confirm = input('Are you sure you want to logout? (y/n): ').lower()
                if confirm in ['y', 'yes']: 
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
            else: print(Color.make_red('\tInvalid option. Please try again.'))
        except Exception as e: print(Color.make_red(e))


def student_system(student_controller):
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        choice = input(Color.make_cyan(
            '\n<BACK|===== Student System =====|'
            '\n1. (R)egister | 2. (L)ogin | 3. (X) Exit'
            '\n👉 Enter your choice (1-3 or first letters): '
        )).strip().lower()
        
        try: 
            if choice in ['1', 'r']:
                print(Color.make_green('\tStudent Sign Up'))
                email = input('\tEnter your email: ').strip().lower()
                
                if Validator.validate_email(email): 
                    password = PasswordSecurer.input_and_confirm_password('\tEnter your password: ')
                    name = input('\tEnter your name: ').strip()
                    if name != '': 
                        student = student_controller.register_student(email, password, name)
                        print(Color.make_yellow(f'\tStudent {student.name} registered successfully with ID {student.student_id}.'))
                    else: raise ValueError('\tName cannot be empty. Please try again')
                
            elif choice in ['2', 'l']:
                print(Color.make_green('\tStudent Sign In'))        
                email = input('\tEnter your email: ').strip().lower()
                password = getpass('\tEnter your password: ')
                student = student_controller.login_student(email, password)
                if student:
                    print(Color.make_yellow(f'\tWelcome {student.name}! You have successfully logged in.'))
                    student_course_system(student_controller)

            elif choice in ['3', 'x']: 
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            else: print(Color.make_red('\tInvalid option. Please try again.'))
        except Exception as e: print(Color.make_red(e))


def student_course_system(student_controller):
    while True:
        choice = input(Color.make_cyan(
            '\n<BACK|===== Student Course System =====|'
            '\n1. (C)hange password'
            '\n2. (E)nroll in a subject'
            '\n3. (R)emove a subject'
            '\n4. (S)how all enrolled subjects'
            '\n5. (X) Logout and back to Student System'
            '\n👉 Enter your choice (1-5 or first letters): '
        )).strip().lower()
        
        try:
            if choice in ['1', 'c']:
                print(Color.make_yellow('\tUpdating Password'))
                old_password = getpass('\tEnter your current password: ')
                
                if student_controller.verify_password(old_password):
                    new_password = PasswordSecurer.input_and_confirm_password('\tEnter your new password: ')
                    student_controller.change_student_password(new_password)

            elif choice in ['2', 'e']: student_controller.enroll_subject()
            elif choice in ['3', 'r']: student_controller.remove_subject_by_id(input('\tSubject ID to remove: ').strip())
            elif choice in ['4', 's']: student_controller.show_enrolled_subjects()
            elif choice in ['5', 'x']: 
                confirm = input('Are you sure you want to logout? (y/n): ').lower() 
                if confirm in ['', 'y', 'yes']:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    student_controller.logout_student()
                    break
            else: print(Color.make_red('\tInvalid option. Please try again.'))
        except Exception as e: print(Color.make_red(e))


if __name__ == '__main__':
    university_system()