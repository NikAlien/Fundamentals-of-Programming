#
# This is the program's UI module. The user interface and all interaction with
# the user (print and input statements) are found here
#
import functions


def separate_instruction(choice):
    instr_list = choice.split()
    return instr_list


def print_list(contestants):
    length = len(contestants)

    if length == 0:
        print("\n No such list")
    else:
        for i in range(length):
            print(functions.to_string(contestants[i], i))


def add(contestants_list, instruction, undo_list, flag):
    if len(instruction) != 4:
        raise ValueError("-1")

    if (not instruction[1].isnumeric()) or (not instruction[2].isnumeric()) or (not instruction[3].isnumeric()):
        raise ValueError("-1")

    p1 = int(instruction[1])
    p2 = int(instruction[2])
    p3 = int(instruction[3])

    if p1 > 10 or p1 < 0 or p2 > 10 or p2 < 0 or p3 > 10 or p3 < 0:
        raise ValueError("Wrong input data: \n   The scores must be between 0 and 10")

    new_contestant = functions.new_participant(p1, p2, p3)
    functions.add_participant(contestants_list, new_contestant)
    if flag == 0:
        undo_list.append(["pop"])


def insert(contestants_list, instruction, undo_list, flag):
    if len(instruction) != 6:
        raise ValueError("-1")

    if (not instruction[1].isnumeric()) or (not instruction[2].isnumeric()) or (not instruction[3].isnumeric()) or instruction[4] != "at" or (not instruction[5].isnumeric()):
            raise ValueError("-1")

    p1 = int(instruction[1])
    p2 = int(instruction[2])
    p3 = int(instruction[3])
    index = int(instruction[5])

    if p1 > 10 or p1 < 0 or p2 > 10 or p2 < 0 or p3 > 10 or p3 < 0:
        raise ValueError("Wrong input data: \n   The scores must be between 0 and 10")

    if index < 0 or index > len(contestants_list) - 1:
        raise ValueError("Wrong input data: \n   Index outside existing list")

    if flag == 0:
        undo_list.append(
            ["insert", contestants_list[index][0], contestants_list[index][1], contestants_list[index][2], "at", index])
    functions.insert_score(contestants_list[index], p1, p2, p3)


def remove(contestants_list, instruction, undo_list, flag):
    length = len(instruction)

    if length == 2:
        if not instruction[1].isnumeric():
            raise ValueError("-1")

        index = int(instruction[1])

        if index < 0 or index > length - 1:
            raise ValueError("Wrong input data: \n   Index outside existing list")

        if flag == 0:
            undo_list.append(
                ["insert", contestants_list[index][0], contestants_list[index][1], contestants_list[index][2], "at", index])
        functions.remove_score(contestants_list[index])

    elif length == 3:
        if (not instruction[2].isnumeric()) or instruction[1] not in ["<", "=", ">"]:
            raise ValueError("-1")

        avg = int(instruction[2])
        indexes = functions.search_participants(contestants_list, instruction[1], avg)
        for i in indexes:
            if flag == 0:
                undo_list.append(
                    ["insert", contestants_list[i][0], contestants_list[i][1], contestants_list[i][2], "at", i])
            functions.remove_score(contestants_list[i])

    elif length == 4:
        if (not instruction[1].isnumeric()) or (not instruction[3].isnumeric()) or instruction[2] != "to":
            raise ValueError("-1")

        start_index = int(instruction[1])
        end_index = int(instruction[3])

        if start_index < 0 or start_index > len(contestants_list) - 1 or end_index < 0 or end_index > len(contestants_list) - 1:
            raise ValueError("Wrong input data: \n   Index outside existing list")

        if start_index > end_index:
            raise ValueError("Wrong input data: \n   Start index is bigger than end index")

        for i in range(start_index, end_index + 1):
            if flag == 0:
                undo_list.append(
                    ["insert", str(contestants_list[i][0]), str(contestants_list[i][1]), str(contestants_list[i][2]), "at", str(i)])
            functions.remove_score(contestants_list[i])

    else:
        raise ValueError("-1")


def replace(contestants_list, instruction, undo_list, flag):
    if len(instruction) != 5:
        raise ValueError("-1")

    if (not instruction[1].isnumeric()) or (not instruction[4].isnumeric()) or instruction[2] not in ["P1", "P2", "P3"] or instruction[3] != "with":
        raise ValueError(
            "Wrong input data: \n Use the following template: \n   replace <old score> <P1 | P2 | P3> with <new score>")

    index = int(instruction[1])
    problem = instruction[2]
    score = int(instruction[4])

    if index < 0 or index > len(contestants_list) - 1:
        raise ValueError("Wrong input data: \n   Index outside existing list")

    if score < 0 or score > 10:
        raise ValueError("Wrong input data: \n   The scores must be between 0 and 10")

    if problem == "P1":
        sc = contestants_list[index][0]
    elif problem == "P2":
        sc = contestants_list[index][1]
    elif problem == "P3":
        sc = contestants_list[index][2]

    if flag == 0:
        undo_list.append(
            ["replace", str(index), str(problem), "with", str(sc)])

    functions.replace_score(contestants_list[index], problem, score)


def list_function(contestants_list, instruction):
    length = len(instruction)
    if length == 1:
        print_list(contestants_list)

    elif length == 2:
        if instruction[1] != "sorted":
            raise ValueError("-1")

        print_list(functions.sort_list(contestants_list[:], "avg"))
    elif length == 3:
        if (not instruction[2].isnumeric()) or instruction[1] not in ["<", "=", ">"]:
            raise ValueError("-1")

        avg = int(instruction[2])
        indexes = functions.search_participants(contestants_list, instruction[1], avg)
        for i in indexes:
            print(functions.to_string(contestants_list[i], i))

    else:
        raise ValueError("-1")


def top(contestants_list, instruction):
    length = len(instruction)

    if length == 2:
        if not instruction[1].isnumeric():
            raise ValueError("-1")

        sorted_list = functions.sort_list(contestants_list[:], "avg")
        nr = int(instruction[1])
        print_list(sorted_list[:nr])

    elif length == 3:
        if (not instruction[2].isnumeric()) or instruction[1] not in ["P1", "P2", "P3"]:
            raise ValueError("-1")

        sorted_list = functions.sort_list(contestants_list[:], instruction[2])
        nr = int(instruction[1])
        print_list(sorted_list[:nr])

    else:
        raise ValueError("\n-1")


def print_menu():
    print("(A) Add the result of a new participant")
    print("   add <P1 score> <P2 score> <P3 score>")
    print("   insert <P1 score> <P2 score> <P3 score> at <position>")

    print("\n(B) Modify scores")
    print("   remove <position>")
    print("   remove <start position> to <end position>")
    print("   replace <old score> <P1 | P2 | P3> with <new score>")

    print("\n(C) Display participants whose score has different properties")
    print("   list")
    print("   list sorted")
    print("   list [ < | = | > ] <score>")

    print("\n(D) Establish the podium")
    print("   top <number>")
    print("   top <number> <P1 | P2 | P3>")
    print("   remove [ < | = | > ] <score>")

    print("\nexit")


def menu(contestants_list):
    undo_list = []
    flag = 0

    while True:
        if flag == 0:
            print("\nChoose your instruction: ")
            print_menu()
            choice = input("--> ")
            instruction = separate_instruction(choice)
        else:
            instruction = undo_list[-1]
            functions.remove_from_list(undo_list)

        if instruction[0] == "add":
            try:
                add(contestants_list, instruction, undo_list, flag)
                flag = 0
            except ValueError as ve:
                if ve == "-1":
                    print("Wrong input data: \n Use one of the following templates: ")
                    print("\n   add <P1 score> <P2 score> <P3 score>")
                else:
                    print(ve)

        elif instruction[0] == "insert":
            try:
                insert(contestants_list, instruction, undo_list, flag)
                flag = 0
            except ValueError as ve:
                if ve == "-1":
                    print("Wrong input data: \n Use one of the following templates: ")
                    print("\n   insert <P1 score> <P2 score> <P3 score> at <position>")
                else:
                    print(ve)

        elif instruction[0] == "remove":
            try:
                remove(contestants_list, instruction, undo_list, flag)
                flag = 0
            except ValueError as ve:
                if ve == "-1":
                    print("Wrong input data: \n Use one of the following templates: ")
                    print("\n   remove <position>")
                    print("\n   remove [ < | = | > ] <score>")
                    print("\n   remove <start position> to <end position>")

                else:
                    print(ve)

        elif instruction[0] == "replace":
            try:
                replace(contestants_list, instruction, undo_list, flag)
                flag = 0
            except ValueError as ve:
                if ve == "-1":
                    print("Wrong input data: \n Use one of the following templates: ")
                    print("\n   replace <old score> <P1 | P2 | P3> with <new score>")
                else:
                    print(ve)

        elif instruction[0] == "list":
            try:
                list_function(contestants_list, instruction)
            except ValueError as ve:
                if ve == "-1":
                    print("Wrong input data: \n Use one of the following templates: ")
                    print("\n   list")
                    print("\n   list sorted")
                    print("\n   list [ < | = | > ] <score>")
                else:
                    print(ve)

        elif instruction[0] == "top":
            try:
                top(contestants_list, instruction)
            except ValueError as ve:
                if ve == "-1":
                    print("Wrong input data: \n Use one of the following templates: ")
                    print("\n   top <number>")
                    print("\n   top <number> <P1 | P2 | P3>")
                else:
                    print(ve)

        elif instruction[0] == "undo":
            if len(undo_list) == 0:
                print("\nNo history of changes")
            else:
                flag = 1

        elif instruction[0] == "exit":
            break

        elif instruction[0] == "pop":
            functions.remove_from_list(contestants_list)
            flag = 0

        else:
            print("\nUnidentifiable instruction")

