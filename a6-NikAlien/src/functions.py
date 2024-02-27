#
# The program's functions are implemented here. There is no user interaction in this file,
# therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions.
#
# Remarks:
#   1. Separate each test in one function
#   2. Use getters because its easier later to change the program
#   3. Debugger can be used to view values of variables in real time
#   4. Think more practical: e.g. Give each student an uniq ID
#   5. Value Error doesn't print right
#   6. undo trouble check
#
import random


def new_participant(p1, p2, p3):
    """
    :param p1: score for problem 1
    :param p2: score for problem 2
    :param p3: score for problem 3
    :return: the new contestant's information in a list
    """
    return [p1, p2, p3]


def get_p1(contestant):
    return contestant[0]


def get_p2(contestant):
    return contestant[1]


def get_p3(contestant):
    return contestant[2]


def set_p1(contestant, value):
    contestant[0] = value


def set_p2(contestant, value):
    contestant[1] = value


def set_p3(contestant, value):
    contestant[2] = value


def insert_score(contestant, p1, p2, p3):
    """

    :param contestant: the contestant from the needed position
    :param p1: score for problem 1
    :param p2: score for problem 2
    :param p3: score for problem 3
    :return:
    """
    set_p3(contestant, p3)
    set_p2(contestant, p2)
    set_p1(contestant, p1)


def to_string(contestant, index):
    """
    Returns information about a contestant in a string format
    :param contestant: the contestant details
    :param index: the contestant's place in the list
    :return: their information in a string
    """
    return f"\nContestant nr.{index}: \n p1 - {contestant[0]}\n p2 - {contestant[1]}\n p3 - {contestant[2]}"


def add_participant(contestants, new_contestant):
    """
    Add a new participant to the already existing list
    :param contestants: the already existing list
    :param new_contestant: the new contestant meant to be added
    :return:
    """
    contestants.append(new_contestant)


def remove_from_list(current_list):
    """
    Remove the last element of list
    :param current_list:
    :return:
    """
    current_list.pop()


def remove_score(contestant):
    """
    Removing the scores of a participant (setting them to 0)
    :param contestant: the contestant that will have 0 as score
    :return:
    """
    set_p3(contestant, 0)
    set_p2(contestant, 0)
    set_p1(contestant, 0)


def replace_score(contestant, prob, score):
    """
    Replace the score from one problem of a specific contestant
    :param contestant: our contestant
    :param prob: the specification of what problem
    :param score: the score
    :return:
    """
    if prob == "P1":
        set_p1(contestant, score)
    elif prob == "P2":
        set_p2(contestant, score)
    elif prob == "P3":
        set_p3(contestant, score)


def average_score(contestant):
    """
    Getting the average score for a contestant
    :param contestant: the contestant's details
    :return: their average score
    """
    average = contestant[0] + contestant[1] + contestant[2]
    average /= 3
    return average


def search_participants(contestants, criteria, avg):
    """
    Find all participants with the needed average score
    :param contestants: the list of all contestants
    :param criteria: the criteria for looking up the needed contestant
    :param avg: the average needed to be searched for
    :return: list of all the necessary contestants
    """
    length = len(contestants)
    needed_indexes = []

    if criteria == "<":
        for i in range(length):
            if average_score(contestants[i]) < avg:
                needed_indexes.append(i)
    elif criteria == "=":
        for i in range(length):
            if average_score(contestants[i]) == avg:
                needed_indexes.append(i)
    elif criteria == ">":
        for i in range(length):
            if average_score(contestants[i]) > avg:
                needed_indexes.append(i)

    return needed_indexes


def random_generator(nr):
    """
    Generating a random list of nr elements
    :param nr: number of elements in the generated list
    :return: the generated list
    """
    random_list = []

    for i in range(nr):
        p1 = random.randint(0, 10)
        p2 = random.randint(0, 10)
        p3 = random.randint(0, 10)
        add_participant(random_list, new_participant(p1, p2, p3))

    return random_list


def sort_list(sorted_list, criteria):
    """
    Sort the given list in reverse order according to the given criteria
    :param sorted_list: list of current contestants
    :param criteria:
    :return: sorted list
    """

    length = len(sorted_list)

    if criteria == "avg":
        for i in range(length):
            sorted_list[i].append(average_score(sorted_list[i]))
        sorted_list.sort(key=lambda x: x[3], reverse=True)

    elif criteria == "P1":
        sorted_list.sort(key=lambda x: x[0], reverse=True)
    elif criteria == "P2":
        sorted_list.sort(key=lambda x: x[1], reverse=True)
    elif criteria == "P3":
        sorted_list.sort(key=lambda x: x[2], reverse=True)

    return sorted_list


def test_function1():
    current_list = [[4, 5, 6]]
    p1 = 1
    p2 = 2
    p3 = 3

    assert new_participant(p1, p2, p3) == [1, 2, 3]

    new_list = new_participant(p1, p2, p3)
    assert get_p1(new_list) == 1
    assert get_p2(new_list) == 2
    assert get_p3(new_list) == 3

    insert_score(new_list, 8, 9, 10)
    assert new_list == [8, 9, 10]

    add_participant(current_list, new_list)
    assert current_list == [[4, 5, 6], [8, 9, 10]]

    for i in range(len(current_list)):
        print(to_string(current_list[i], i))

    remove_from_list(current_list)
    assert current_list == [[4, 5, 6]]

    remove_score(current_list[0])
    assert current_list == [[0, 0, 0]]

    replace_score(current_list[0], "P1", 4)
    replace_score(current_list[0], "P2", 5)
    replace_score(current_list[0], "P3", 6)
    assert current_list == [[4, 5, 6]]

    assert average_score(current_list[0]) == 5


def test_function2():
    current_list = [[4, 5, 6], [1, 2, 3], [3, 10, 8], [0, 0, 0]]
    ind = search_participants(current_list, "<", 3)
    assert ind == [1, 3]

    sorted_list = sort_list(current_list[:], "avg")
    assert sorted_list == [[3, 10, 8, 7], [4, 5, 6, 5], [1, 2, 3, 2], [0, 0, 0, 0]]

    sorted_list2 = sort_list(current_list[:], "P1")
    assert sorted_list2 == [[4, 5, 6, 5], [3, 10, 8, 7], [1, 2, 3, 2], [0, 0, 0, 0]]


test_function1()
test_function2()



