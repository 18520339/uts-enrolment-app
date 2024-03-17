import re

class Utils:
    # Constants for validation patterns
    EMAIL_PATTERN = re.compile(r'^[a-zA-Z]+.[a-zA-Z]+@university\.com$')
    PASSWORD_PATTERN = re.compile(r'^[A-Z][a-zA-Z]{6,}\d{3,}$')

    @staticmethod
    def validate_email(email: str) -> bool:
        return bool(Utils.EMAIL_PATTERN.match(email))

    @staticmethod
    def validate_password(password: str) -> bool:
        return bool(Utils.PASSWORD_PATTERN.match(password))

    @staticmethod
    def calculate_grade(mark: int) -> str:
        # Calculates the grade based on the mark
        if mark is None: return None
        if mark < 50: return 'Z'
        elif 50 <= mark < 65: return 'P'
        elif 65 <= mark < 75: return 'C'
        elif 75 <= mark < 85: return 'D'
        return 'HD'

    @staticmethod
    def display_students_table(students: List[Student], column_config: dict = {}) -> None:
        if students is None or len(students) == 0:
            print('<No students to display>')
            return
        
        columns = { # Format key: (header name, value function, width)
            'student_id': ('ID', lambda s: s.student_id, 10), 
            'name': ('Name', lambda s: s.name, 20),
            'email': ('Email', lambda s: s.email, 30),
            'subjects_cnt': ('Subjects Enrolled', lambda s: len(s.subjects), 20),
            'average_mark': ('Avg. Mark', lambda s: s.average_mark, 20),
            'overall_grade': ('Grade', lambda s: s.overall_grade, 20)
        }

        header, separator = '\n|', '-'
        for key, value in columns.items():
            if column_config.get(key, True):
                header += f' {value[0]}:<{value[2]} |'
                separator += '-' * (value[2] + 3)

        for student in students:
            row = '|'
            for key, value in columns.items():
                if column_config.get(key, True):
                    row += f' {value[1](student):<{value[2]}} |'
            print(row)