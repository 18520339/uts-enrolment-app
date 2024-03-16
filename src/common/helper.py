import re
import random


class Utils:
    # Constants for validation patterns
    EMAIL_PATTERN = re.compile(r'^[a-zA-Z]+.[a-zA-Z]+@university\.com$')
    PASSWORD_PATTERN = re.compile(r'^[A-Z][a-zA-Z]{6,}\d{3,}$')

    @staticmethod
    def validate_email(email: str) -> bool:
        return bool(EMAIL_PATTERN.match(email))

    @staticmethod
    def validate_password(password: str) -> bool:
        return bool(PASSWORD_PATTERN.match(password))
    
    @staticmethod
    def generate_student_id() -> str:
        # Generate a unique 6-digit student ID.
        return str(random.randint(1, 999999)).zfill(6)

    @staticmethod
    def generate_subject_id() -> str:
        # Generate a unique 3-digit subject ID.
        return str(random.randint(1, 999)).zfill(3) 

    @staticmethod
    def generate_subject_name():
        # Generate a random subject name
        return random.choice(['Computer Science', 'Mathematics', 'Physics', 'Chemistry', 'Biology'])

    @staticmethod
    def generate_subject_mark():
        # Generate a random subject mark between 25 and 100
        return random.randint(25, 100)
