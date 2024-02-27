import unittest

from src.domain.student import Student
from src.repository.repo import MemoryRepository
from src.services.services import Services
from src.domain.student_validator import StudentValidator

class TestServices(unittest.TestCase):
    def test_services(self):

        student_list = MemoryRepository()
        student_validation = StudentValidator()

        student1 = Student(1, "Nik", 911)
        student2 = Student(2, "Amy", 912)
        student3 = Student(3, "Dan", 911)


        student_list.add(student1)
        student_list.add(student2)
        student_list.add(student3)

        serv = Services(student_list, student_validation)

        serv.add_new_student(4, "Lea", 911)
        assert len(student_list) == 4

        serv.delete_according_to_group(911)
        assert len(student_list) == 1


    def test_undo(self):
        student_list_original = MemoryRepository()
        student_list_modified = MemoryRepository()
        student_validation = StudentValidator()

        student1 = Student(1, "Nik", 911)
        student2 = Student(2, "Amy", 912)
        student3 = Student(3, "Dan", 911)

        student_list_original.add(student1)
        student_list_original.add(student2)
        student_list_original.add(student3)

        student_list_modified.add(student1)
        student_list_modified.add(student2)
        student_list_modified.add(student3)

        serv = Services(student_list_modified, student_validation)

        serv.add_new_student(4, "Lea", 911)
        assert len(student_list_modified) == 4

        serv.undo()

        for stud1 in student_list_original.get_list_students():
            for stud2 in student_list_original.get_list_students():
                if stud1 == stud2:
                    assert stud1.student_id == stud2.student_id
