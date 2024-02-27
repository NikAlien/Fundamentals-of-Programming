class Student:
    """
    Each student has:
        -> id (integer and unique)
        -> name (string)
        -> group (positive integer)
    """
    def __init__(self, student_id: int, name: str, group: int):
        self.__student_id = student_id
        self.__name = name
        self.__group = group

    @property
    def student_id(self):
        return self.__student_id

    @property
    def name(self):
        return self.__name

    @property
    def group(self):
        return self.__group

    def __str__(self):
        return str(self.student_id) + ") " + self.name + ", gr." + str(self.group)
