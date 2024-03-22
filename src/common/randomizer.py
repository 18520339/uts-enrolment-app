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
    def generate_subject_name() -> str:
        # Generate a random subject name
        subject_names = ['Database', 'Network', 'Programming', 'Mathematics', 'Physics', 'Chemistry', 'Biology']
        subject_levels = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
        return random.choice(subject_names) + ' ' + random.choice(subject_levels)

    @staticmethod
    def generate_subject_mark() -> int:
        # Generate a random subject mark between 25 and 100
        return random.randint(25, 100)