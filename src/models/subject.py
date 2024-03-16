from common.helper import Utils

class Subject:
    def __init__(self, name='', mark=0):
        self._subject_id = Utils.generate_subject_id()
        self._name = name
        self.mark = mark # Ensure the value passed to constructor has same validation defined in setter
        self._grade = None # Grade will be calculated based on the mark

    @property
    def subject_id(self):
        return self._subject_id

    @property
    def name(self):
        return self._name

    @property
    def mark(self):
        return self._mark

    @property
    def grade(self):
        return self._grade

    @mark.setter
    def mark(self, value: int):
        # Assigns a mark to the subject and calculates the grade based on the mark.
        if 0 <= value <= 100:
            self._mark = value
            self._grade = self.calculate_grade(value)
        else: raise ValueError('Mark must be between 0 and 100.')

    @staticmethod
    def calculate_grade(mark) -> str:
        # Calculates the grade based on the mark.
        if mark is None: return None
        if mark < 50: return 'Z'
        elif 50 <= mark < 65: return 'P'
        elif 65 <= mark < 75: return 'C'
        elif 75 <= mark < 85: return 'D'
        return 'HD'

    def __str__(self):
        # Returns a string representation of the subject, useful for debugging.
        return f'Subject ID: {self.subject_id}, Name: {self.name}, Mark: {self.mark}, Grade: {self.grade}'