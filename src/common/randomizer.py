import random

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