import random


def create_flight(code, duration, departure, destination):
    """

    :param code:
    :param duration:
    :param departure:
    :param destination:
    :return: Returns the new flight with the given details
    """
    return [code, duration, departure, destination]


def get_code(flight):
    return flight[0]


def get_duration(flight):
    return flight[1]


def get_departure_city(flight):
    return flight[2]


def get_destination_city(flight):
    return flight[3]

def set_duration(flight, minutes):
    flight[1] = minutes

def add_flight(flights_list, new_flight):
    """
    Adds the new flight to the already existing list
    :param flights_list:
    :param new_flight:
    :return:
    """
    flights_list.append(new_flight)

def search_by_code(flights_list, code):
    for flight in flights_list:
        if get_code(flight) == code:
            return True
    return False

def string_flight(flight):
    """
    :param flight:
    :return: Flight converted in string
    """
    return get_code(flight) + " / " + str(get_duration(flight)) + "min / " + get_departure_city(flight) + " --> " + get_destination_city(flight)


def delete_flight(code, flights_list):
    """
    Deletes the flight with the given code from the list
    :param code:
    :param flights_list:
    :return:
    """
    length = len(flights_list)

    for index in range(length):
        if get_code(flights_list[index]) == code:
            flights_list.pop(index)
            break


def choose_flights_by_departure(departure, flights_list):
    """
    Chooses the flights from whole list according to the given departure city
    :param departure:
    :param flights_list:
    :return: the list of these flights
    """
    departure_flights = []

    for flight in flights_list:
        if get_departure_city(flight) == departure:
            departure_flights.append(flight)

    return departure_flights

def sort_by_destination(departure_list):
    """
    Sorts the given list by destination city
    :param departure_list:
    :return:
    """
    sorted_list = sorted(departure_list, key= lambda x: get_destination_city(x))
    return sorted_list

def generate_random_flights(n):
    """
    Generates n random flights for the start of the program
    :param n:
    :return:
    """
    flights_list = []

    code_version = []
    for i in range(10):
        code_version.append(str(i))

    c = ["A", "B", "C", "D", "E", "F"]
    for i in range(len(c)):
        code_version.append(c[i])

    departure_cities = ["Cluj-Napoca", "Chisinau", "Balti", "Iasi", "Kiev"]
    destination_cities = ["London", "Paris", "Berlin", "Atlanta"]

    for i in range(n):
        length = random.randint(3, 6)
        code = ""
        for j in range(length):
            code += random.choice(code_version)

        duration = random.randint(20, 60)
        departure = random.choice(departure_cities)
        destination = random.choice(destination_cities)
        new_flight = create_flight(code, duration, departure, destination)
        add_flight(flights_list, new_flight)

    return flights_list

def increase_duration(flights_list, departure, minutes):
    """
    Increases the duration of every flight from a given departure with the given minutes
    :param flights_list:
    :param departure:
    :param minutes:
    :return:
    """
    for flight in flights_list:
        if get_departure_city(flight) == departure:
            set_duration(flight, get_duration(flight) + minutes)


def test_get():
    flight = ["0DGY3", 45, "Chisinau", "London"]
    assert get_code(flight) == "0DGY3"
    assert get_duration(flight) == 45
    assert get_departure_city(flight) == "Chisinau"
    assert get_destination_city(flight) == "London"

def test_increase():
    flight = [["0DGY3", 45, "Chisinau", "London"]]
    increase_duration(flight, get_departure_city(flight[0]), 40)
    assert get_duration(flight[0]) == 85

def test_delete():
    flights = [["0DGY3", 45, "Chisinau", "London"], ["HGJF", 30, "Balti", "London"], ["67GHJ", 90, "Balti", "Atlanta"]]
    flights_del = [['HGJF', 30, 'Balti', 'London'], ['67GHJ', 90, 'Balti', 'Atlanta']]

    delete_flight("0DGY3", flights)
    assert  flights == flights_del

def test_sort_by_choice():
    flights = [["0DGY3", 45, "Chisinau", "London"], ["HGJF", 30, "Balti", "London"], ["67GHJ", 90, "Balti", "Atlanta"], ['GHFH', 45, 'Balti', 'Berlin']]
    chosen_flights = choose_flights_by_departure("Balti", flights)
    chosen_flights = sort_by_destination(chosen_flights)

    flights_right = [['67GHJ', 90, 'Balti', 'Atlanta'], ['GHFH', 45, 'Balti', 'Berlin'], ['HGJF', 30, 'Balti', 'London']]

    assert chosen_flights == flights_right

def test_search():
    flights = [["0DGY3", 45, "Chisinau", "London"], ["HGJF", 30, "Balti", "London"], ["67GHJ", 90, "Balti", "Atlanta"]]
    assert search_by_code(flights, "HGJF") == True
    assert search_by_code(flights, "H6JF") == False


# test_get()
# test_increase()
# test_delete()
# test_sort_by_choice()
# test_search()