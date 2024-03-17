import re
import random
import string
import secrets
import hashlib


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
    def calculate_grade(mark: int) -> str:
        # Calculates the grade based on the mark
        if mark is None: return None
        if mark < 50: return 'Z'
        elif 50 <= mark < 65: return 'P'
        elif 65 <= mark < 75: return 'C'
        elif 75 <= mark < 85: return 'D'
        return 'HD'

    @staticmethod
    def display_students_table(students: List[Student], column_config: dict = {}):
        columns = { # Format key: (header name, value function, width)
            'student_id': ('ID', lambda s: s.student_id, 10), 
            'name': ('Name', lambda s: s.name, 20),
            'email': ('Email', lambda s: s.email, 30),
            'subjects_cnt': ('Subjects Enrolled', lambda s: len(s.subjects), 20),
            'average_mark': ('Avg. Mark', lambda s: s.average_mark, 20),
            'overall_grade': ('Grade', lambda s: s.overall_grade, 20)
        }

        header, separator = '|', '-'
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
            

class Randomizer:
        
    @staticmethod
    def generate_student_id() -> str:
        # Generate a unique 6-digit student ID
        return str(random.randint(1, 999999)).zfill(6)

    @staticmethod
    def generate_subject_id() -> str:
        # Generate a unique 3-digit subject ID
        return str(random.randint(1, 999)).zfill(3) 

    @staticmethod
    def generate_subject_name():
        # Generate a random subject name
        return random.choice(['Computer Science', 'Mathematics', 'Physics', 'Chemistry', 'Biology'])

    @staticmethod
    def generate_subject_mark():
        # Generate a random subject mark between 25 and 100
        return random.randint(25, 100)


class PasswordSecurer:
    salt_length = 32  # The length of the salt in bytes
    hash_name = 'sha256'  # The name of the hash digest algorithm to use
    hash_iterations = 100000 # It is recommended to use >= 100,000 iterations of SHA-256 

    @staticmethod
    def generate_temp_password(length: int) -> str:
        # Generates a secure temporary password
        alphabet = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(string.printable) for i in range(length))

    @staticmethod
    def hash_password(password: str) -> str:
        # Hashes a password with a randomly generated salt
        salt = os.urandom(salt_length)  # A new salt for this user
        key = hashlib.pbkdf2_hmac(
            hash_name, # The hash digest algorithm
            password.encode('utf-8'), # Convert the password to bytes
            salt = salt, # Provide the salt
            iterations = hash_iterations  
        )
        storage = salt + key # Store the salt and key together
        return storage.hex() # Return the hashed password as hex digits for storage

    @staticmethod
    def verify_password(stored_password: bytes, provided_password: str) -> bool:
        # Verifies a provided password against the stored hash.
        stored_password_bytes = bytes.fromhex(stored_password)
        new_key = hashlib.pbkdf2_hmac(
            hash_name,
            provided_password.encode('utf-8'),
            salt = stored_password_bytes[:salt_length], # The salt is the first 32 bytes
            iterations = hash_iterations
        )
        return new_key == stored_password_bytes[salt_length:] # The key is the last 32 bytes