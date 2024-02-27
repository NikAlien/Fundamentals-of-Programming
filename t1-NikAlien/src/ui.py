import functions

def print_menu():
    print("\nChoose your action: ")
    print("1. Add new flight ")
    print("2. Delete a given flight")
    print("3. Show all flights from a departure city")
    print("4. Print the whole list")
    print("5. Departure city with strong winds increase time")
    print("6. Exit")


def add_new_flight(flights_list):
    print("\nGive necessary data: ")
    code = input("Code --> ")
    if len(code) < 3:
        raise ValueError("Code must be longer than 3 characters")

    if functions.search_by_code(flights_list, code):
        raise ValueError("Code already in list")

    duration = int(input("Duration --> "))
    if duration < 20:
        raise ValueError("Duration must be >= 20")
    departure = input("Departure city --> ")
    if len(departure) < 3:
        raise ValueError("Departure must be longer than 3 characters")
    destination = input("Destination city --> ")
    if len(destination) < 3:
        raise ValueError("Destination must be longer than 3 characters")

    new_flight = functions.create_flight(code, duration, departure, destination)
    functions.add_flight(flights_list, new_flight)


def delete_given_flight(flights_list):
    print("\nGive necessary data: ")
    code = input("Code --> ")
    if functions.search_by_code(flights_list, code) == 0:
        raise ValueError("No such code in list")
    functions.delete_flight(code, flights_list)


def print_flights_by_departure(flights_list):
    print("\nGive necessary data: ")
    departure = input("Departure city --> ")
    departure_flights = functions.choose_flights_by_departure(departure, flights_list)
    departure_flights = functions.sort_by_destination(departure_flights)

    for flight in departure_flights:
        print(functions.string_flight(flight))

def print_flights(flights_list):
    for flight in flights_list:
        print(functions.string_flight(flight))


def increase_time_flights(flights_list):
    print("\nGive necessary data: ")
    departure = input("Departure city --> ")
    minutes = int(input("Minutes --> "))
    if minutes < 10 or minutes > 60:
        raise ValueError("Duration must be between 10 and 60")

    functions.increase_duration(flights_list, departure, minutes)


def menu(flights_list):
        while True:
            print_menu()
            choice = int(input("--> "))
            if choice == 1:
                try:
                    add_new_flight(flights_list)
                except ValueError as ve:
                    print(ve)
            elif choice == 2:
                try:
                    delete_given_flight(flights_list)
                except ValueError as ve:
                    print(ve)
            elif choice == 3:
                print_flights_by_departure(flights_list)
            elif choice == 4:
                print_flights(flights_list)
            elif choice == 6:
                break
            elif choice == 5:
                try:
                    increase_time_flights(flights_list)
                except ValueError as ve:
                    print(ve)
            else:
                print("Unidentifiable comment")