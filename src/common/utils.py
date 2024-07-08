import os
import re
import random


class Validator:
    DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'students.data')
    EMAIL_PATTERN = r'^[a-zA-Z0-9]+\.[a-zA-Z0-9]+@university\.com$'
    PASSWORD_PATTERN = r'^[A-Z][a-zA-Z]{5,}\d{3,}$'

    @staticmethod
    def validate_email(email: str) -> bool:
        pattern = re.compile(Validator.EMAIL_PATTERN)
        if bool(pattern.match(email.lower())): return True
        raise ValueError('\tEmail must be in the form of firstname.lastname@university.com.')

    @staticmethod
    def validate_password(password: str) -> bool:
        pattern = re.compile(Validator.PASSWORD_PATTERN)
        if bool(pattern.match(password)): return True
        raise ValueError('\tPassword must start with UPPERCASE, followed by >= 5 letters and >= 3 digits.')
    
    
class Randomizer:
        
    @staticmethod
    def generate_student_id() -> str:
        return str(random.randint(1, 999999)).zfill(6) # Generate a unique 6-digit student ID

    @staticmethod
    def generate_subject_id() -> str:
        return str(random.randint(1, 999)).zfill(3) # Generate a unique 3-digit subject ID

    @staticmethod
    def generate_subject_name() -> str:
        subject_names = ['Database', 'Network', 'Programming', 'Mathematics', 'Physics', 'Chemistry', 'Biology']
        subject_levels = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
        return random.choice(subject_names) + ' ' + random.choice(subject_levels) # Generate a random subject name

    @staticmethod
    def generate_subject_mark() -> int:
        return random.randint(25, 100) # Generate a random subject mark between 25 and 100