from src.domain.validatorException import ValidatorException
from src.domain.student import Student
class StudentValidator:
    def __init__(self):
        self._errors = ""

    def _groupValid(self, group):
        if group is None:
            return False
        if group <= 0:
            return False

    def validate(self, student):
        if not isinstance(student, Student):
            raise TypeError("Can only validate Student objects!")
        self._errors = []
        if student.student_id is None:
            self._errors.append("Student must have an id")
        if len(student.name) == 0:
            self._errors.append("Student must have a name")
        if self._groupValid(student.group) == False:
            self._errors.append("Group nr doesn't satisfy the conditions set")
        if len(self._errors) > 0:
            raise ValidatorException(self._errors)
        return True
