import os
from controllers.student_controller import StudentController
from controllers.admin_controller import AdminController


def university_system():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Welcome to the University Enrollment System')
        print('1. (A)dmin | 2. (S)tudent | 3. (E)xit')
        choice = input('Enter your choice (1-3 or first letters):')

        if choice == '1' or choice.lower() == 'a': 
            admin_controller = AdminController()
            admin_system(admin_controller)
            
        elif choice == '2' or choice.lower() == 's': 
            student_controller = StudentController()
            student_system(student_controller)

        elif choice == '3' or choice.lower() == 'e': exit()
        else: print('Invalid option. Please try again.')


def admin_system(admin_controller):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n--- Admin System ---')
    print('1. (C)lear all student data')
    print('2. (G)roup students by grade')
    print('3. (P)artition students by performance')
    print('4. (R)emove a student by ID')
    print('5. (S)how all registered students')
    print('6. (X) Logout and back to University System')

    while True:
        choice = input('Enter your choice (1-6 or first letters):')
        if choice == '1' or choice.lower() == 'c': 
            admin_controller.clear_database()
        elif choice == '2' or choice.lower() == 'g': 
            admin_controller.group_students_by_grade()
        elif choice == '3' or choice.lower() == 'p':
            admin_controller.partition_students_performance()
        elif choice == '4' or choice.lower() == 'r':
            student_id = input('Enter the student ID to remove: ')
            admin_controller.remove_student_by_id(student_id)
        elif choice == '5' or choice.lower() == 's':
            admin_controller.show_registered_students()
        elif choice == '6' or choice.lower() == 'x':
            confirm = input('Are you sure you want to logout? (y/n): ')
            if confirm.lower() == 'y': break
        else:
            print('Invalid option. Please try again.')
            

def student_system(student_controller):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n--- Student System ---')
        print('1. (R)egister')
        print('2. (L)ogin')
        print('3. (X) Logout and back to University System')
        choice = input('Enter your choice (1-3 or first letters): ')

        if choice == '1' or choice.lower() == 'r':
            print('\nStudent Sign Up')
            name = input('Enter your name: ')
            email = input('Enter your email: ')
            password = input('Enter your password: ')
            try: 
                student = student_controller.register_student(name, email, password)
                if student:
                    print(f'Student {student.name} registered successfully with ID {student.student_id}.')
            except Exception as e: print(e)

        elif choice == '2' or choice.lower() == 'l':
            print('\nStudent Sign In')
            email = input('Enter your email: ')
            password = input('Enter your password: ')
            try:
                student = student_controller.login_student(email, password)
                if student:
                    print(f'Welcome {student.name}! You have successfully logged in.')
                    student_course_system(student_controller)
            except Exception as e: print(e)

        elif choice == '3' or choice.lower() == 'x': 
            confirm = input('Are you sure you want to logout? (y/n): ')
            if confirm.lower() == 'y':
                student_controller.logout_student()
                break
        else: print('Invalid option. Please try again.')


def student_course_system(student_controller):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n--- Student Course System ---')
    print('1. (C)hange password')
    print('2. (E)nroll in a subject')
    print('3. (R)emove a subject')
    print('4. (S)how all enrolled subjects')
    print('5. (X) Back to Student System')

    while True:
        choice = input('Enter your choice (1-5 or first letters): ')

        if choice == '1' or choice.lower() == 'c':
            old_password = input('Enter your old password: ')
            new_password = input('Enter your new password: ')
            try:
                student_controller.change_student_password(old_password, new_password)
            except Exception as e: print(e)

        if choice == '2' or choice.lower() == 'e':
            student_controller.enroll_random_subject()

        elif choice == '3' or choice.lower() == 'r':
            subject_id = input('Enter subject ID to remove: ')
            student_controller.remove_subject(subject_id)

        elif choice == '4' or choice.lower() == 's':
            student_controller.show_enrolled_subjects(student)

        elif choice == '5' or choice.lower() == 'x': break
        else: print('Invalid option. Please try again.')


if __name__ == '__main__':
    university_system()