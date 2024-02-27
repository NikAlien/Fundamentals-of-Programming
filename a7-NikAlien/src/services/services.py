from src.domain.student import Student
from src.services.ServicesException import ServicesException

class Services:
    def __init__(self, repository, validator):
        self._student_list = repository
        self._validator = validator
        self._history = []

    def give_student_list_to_ui(self):
        """
        Return list of students sorted ascending according to their id
        :return:
        """
        student_list = self._student_list.get_list_students()
        return sorted(student_list, key= lambda x: x.student_id)

    def delete_according_to_group(self, group):
        """
        Finds all instances of the group in the list and then deletes them from the list by id
        :param group:
        :return:
        """
        ids = []

        for student_info in self._student_list.get_list_students():
            if student_info.group == group:
                ids.append(student_info)
                self._history.append(["add", student_info])

        if len(ids) == 0:
            raise ServicesException("Group not in the list")

        for stud_id in ids:
            self._student_list.delete(stud_id.student_id)


    def add_new_student(self, student_id, name, group):
        """
        Adds new student to the repository
        :return:
        """
        new_student = Student(student_id, name, group)
        self._validator.validate(new_student)

        self._student_list.add(new_student)
        self._history.append(["delete", new_student])


    def undo(self):
        """
        Undos the last action of the user
        :return:
        """
        index = len(self._history) - 1

        if index < 0:
            raise ServicesException("No more history recorded")

        if self._history[index][0] == "add":
            while index > 0 and self._history[index][0] == "add":
                self._student_list.add(self._history[index][1])
                self._history.pop(index)
                index -= 1

        elif index >= 0 and self._history[index][0] == "delete":
            self._student_list.delete(self._history[index][1].student_id)
            self._history.pop(index)
