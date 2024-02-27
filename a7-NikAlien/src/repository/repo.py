import pickle
from src.domain.student import Student
from src.repository.repository_exception import RepositoryException

class MemoryRepository:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def search(self, stud_id):
        for student in self._data:
            if stud_id == student.student_id:
                return student
        return None

    def get_list_students(self):
        return self._data

    def add(self, new_student: Student):
        if self.search(new_student.student_id) is not None:
            raise RepositoryException("Student id already present in the list")
        self._data.append(new_student)

    def delete(self, student_id):
        student = self.search(student_id)
        if student is None:
            raise RepositoryException("Element not in repository")
        self._data.remove(student)

class TextFileRepository(MemoryRepository):
    def __init__(self, file_name = "students.txt"):
        super(TextFileRepository, self).__init__()

        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        fin = open(self._file_name, "rt")
        lines = fin.readlines()
        fin.close()

        for line in lines:
            student_line = line.split(",")
            new_student = Student(int(student_line[0]), student_line[1], int(student_line[2].strip()))
            super().add(new_student)

    def _save_file(self):
        fout = open(self._file_name, "wt")

        for student_line in self.get_list_students():
            student_line = str(student_line.student_id) + "," + student_line.name + "," + str(student_line.group) + "\n"
            fout.write(student_line)

        fout.close()

    def delete(self, student_id):
        super().delete(student_id)
        self._save_file()

    def add(self, new_student: Student):
        super().add(new_student)
        self._save_file()
        

class BinaryFileRepository(MemoryRepository):
    def __init__(self, file_name = "students.bin"):
        super(BinaryFileRepository, self).__init__()
        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        fin = open(self._file_name, "rb")
        students = pickle.load(fin)

        for student_line in students:
            super().add(student_line)
        fin.close()

    def _save_file(self):
        fout = open(self._file_name, "wb")
        pickle.dump(self.get_list_students(), fout)
        fout.close()

    def delete(self, student_id):
        super().delete(student_id)
        self._save_file()

    def add(self, new_student: Student):
        super().add(new_student)
        self._save_file()

