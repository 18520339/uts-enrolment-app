from .randomizer import Randomizer
from .securer import PasswordSecurer
import os
import re

class Utils:
    DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'students.data')
    EMAIL_PATTERN = r'^[a-zA-Z0-9]+.[a-zA-Z0-9]+@university\.com$'
    PASSWORD_PATTERN = r'^[A-Z][a-zA-Z]{5,}\d{3,}$'

    @staticmethod
    def validate_email(email: str) -> bool:
        pattern = re.compile(Utils.EMAIL_PATTERN)
        if bool(pattern.match(email.lower())): return True
        print('Email must be in the form of firstname.lastname@university.com.')
        return False

    @staticmethod
    def validate_password(password: str) -> bool:
        pattern = re.compile(Utils.PASSWORD_PATTERN)
        if bool(pattern.match(password)): return True
        print('Password must start with UPPERCASE, followed by >= 5 letters and >= 3 digits.')
        return False
    
class Color:
    
    @staticmethod
    def make_red(text):
        return f'\033[91m {text}\033[00m'

    @staticmethod
    def make_yellow(text):
        return f'\033[93m {text}\033[00m'
        
    @staticmethod
    def make_cyan(text):
        return f'\033[96m {text}\033[00m'

    @staticmethod
    def make_green(text):
        return f'\033[92m {text}\033[00m'