from src.services.services import Services
class UI:
    def __init__(self, services: Services):
        self._commands = {'+': self.add_student, 'd': self.display_list, '-': self.delete_from_list, 'u': self.undo_list}
        self._service = services

    def print_menu(self):
        """
        Print the menu
        """
        print("\nChoose your option: ")
        print("  display the list --> d")
        print("  add new student --> +")
        print("  delete students from a specific group --> -")
        print("  undo the last operation --> u")
        print("  exit program --> x")

    def add_student(self):
        student_id = int(input("Student id --> "))
        name = input("Name --> ")
        group = int(input("Group --> "))

        self._service.add_new_student(student_id, name, group)

    def display_list(self):
        for stud in self._service.give_student_list_to_ui():
            print(stud)

    def delete_from_list(self):
        group = int(input("Group --> "))
        self._service.delete_according_to_group(group)

    def undo_list(self):
        self._service.undo()

    def start(self):

        while True:
            self.print_menu()
            _choice = input("\nCommand: ")

            if _choice == "x":
                return

            if _choice  not in self._commands:
                print("Unidentifiable command")

            else:
                try:
                    self._commands[_choice]()
                except Exception as ve:
                    print("Error: " + str(ve))
