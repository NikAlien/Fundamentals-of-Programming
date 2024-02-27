import unittest

from src.domain.student import Student
from src.repository.repository_exception import RepositoryException
from src.repository.repo import MemoryRepository

class TestStudentRepo(unittest.TestCase):
    def test_student_repo(self):
        repo = MemoryRepository()
        assert len(repo) == 0

        repo.add(Student(1, "Nik", 911))
        repo.add(Student(2, "Amy", 912))
        repo.add(Student(3, "Dan", 911))
        assert len(repo) == 3

        try:
            repo.add(Student(2, "Amy", 912))
            assert False
        except RepositoryException:
            assert True

        repo.delete(2)
        assert len(repo) == 2
