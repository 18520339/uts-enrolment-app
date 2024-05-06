import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from controllers import AdminController, StudentController
from common import Utils, Color


def university_system():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        choice = input(Color.make_cyan('University System: (A)dmin, (S)tudent, or X : ')).strip().upper()
        if choice == 'A': admin_system(AdminController())
        elif choice == 'S': student_system(StudentController())
        elif choice == 'X': 
            print(Color.make_yellow('Thank You'))
            exit()
        else: print(Color.make_red('Invalid option. Please try again'))


def admin_system(admin_controller):
    while True:
        choice = input(Color.make_cyan('\tAdmin System (c/g/p/r/s/x): ')).strip().lower()
        if choice == 'c': 
            print(Color.make_yellow('\tClearing students database'))
            confirm = input(Color.make_red('\tAre you sure want to clear the database (Y)ES/(N)O: ')).strip().upper()
            if confirm in ['Y', 'YES']: admin_controller.clear_database()
                
        elif choice == 'g': admin_controller.group_students_by_grade()
        elif choice == 'p': admin_controller.partition_students_by_pass_fail()
        elif choice == 'r': admin_controller.remove_student_by_id(input('\tRemove by ID: ').strip())
        elif choice == 's': admin_controller.show_registered_students()
        elif choice == 'x': break
        else: print(Color.make_red('\tInvalid option. Please try again'))
            

def student_system(student_controller):
    while True:
        choice = input(Color.make_cyan('\tStudent System (l/r/x): ')).strip().lower()
                
        if choice == 'r':
            print(Color.make_green('\tStudent Sign Up'))
            while True:
                email = input('\tEmail: ').strip().lower()
                password = input('\tPassword: ')
                try: 
                    if Utils.validate_email(email) and Utils.validate_password(password):
                        print(Color.make_yellow('\temail and password formats acceptable.'))
                        student = student_controller.register_student(email, password)
                        if student: 
                            print(Color.make_yellow(f'\tEnrolling Student {student.name}'))
                            break
                    else: print(Color.make_red('\tInvalid email or password format'))
                except Exception as e: 
                    print(Color.make_red(e))
                    break
            
        elif choice == 'l':
            print(Color.make_green('\tStudent Sign In'))
            while True:
                email = input('\tEmail: ').strip().lower()
                password = input('\tPassword: ')
                try: 
                    if Utils.validate_email(email) and Utils.validate_password(password):
                        print(Color.make_yellow('\temail and password formats acceptable.'))
                        student = student_controller.login_student(email, password)
                        if student: 
                            student_course_system(student_controller)
                            break
                    else: print(Color.make_red('\tInvalid email or password format'))
                except Exception as e: 
                    print(Color.make_red(e))
                    break

        elif choice == 'x': break
        else: print(Color.make_red('\tInvalid option. Please try again'))


def student_course_system(student_controller):
    while True:
        choice = input(Color.make_cyan('\t\tStudent Course Menu (c/e/r/s/x): ')).strip().lower()
        
        if choice == 'c':
            print(Color.make_yellow('\t\tUpdating Password'))
            new_password = input('\t\tNew Password: ')
            if not Utils.validate_password(new_password):
                print(Color.make_red('\t\tInvalid password format'))
                continue

            while True:
                confirm_password = input('\t\tConfirm Password: ')
                if new_password != confirm_password:
                    print(Color.make_red('\t\tPasswords does not match - try again'))
                    continue
                try: student_controller.change_student_password(new_password)
                except Exception as e: print(Color.make_red(e))
                break

        elif choice == 'e': student_controller.enroll_subject()
        elif choice == 'r': student_controller.remove_subject_by_id(input('\t\tRemove by ID: ').strip())
        elif choice == 's': student_controller.show_enrolled_subjects()
        elif choice == 'x': 
            student_controller.logout_student()
            break
        else: print(Color.make_red('\t\tInvalid option. Please try again'))


if __name__ == '__main__':
    university_system()