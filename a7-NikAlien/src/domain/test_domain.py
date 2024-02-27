import unittest
from src.domain.student import Student

class TestDomain(unittest.TestCase):
    def test_domain(self):

        student_test = Student(1, "Nik", 911)
        assert student_test.student_id == 1
        assert student_test.name == "Nik"
        assert student_test.group == 911

        assert str(student_test) == "1) Nik, gr.911"
