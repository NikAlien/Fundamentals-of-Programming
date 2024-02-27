import functions
import ui


flights_list = functions.generate_random_flights(5)
ui.menu(flights_list)