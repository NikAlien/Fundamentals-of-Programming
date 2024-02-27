from src.domain.student import Student
from src.repository.repo import MemoryRepository

class RepositoryStudents:
    def generate_repo(self, student_list: MemoryRepository):
        student_list.add(Student(1, "Nik", 911))
        student_list.add(Student(2, "Amy", 912))
        student_list.add(Student(3, "Dan", 911))
        student_list.add(Student(4, "Igor", 913))
        student_list.add(Student(5, "Cataly", 913))
        student_list.add(Student(6, "Eva", 912))
        student_list.add(Student(7, "Dan", 911))
        student_list.add(Student(8, "Vanea", 912))
        student_list.add(Student(9, "Ale", 911))
        student_list.add(Student(10, "Dragos", 913))

        return student_list
