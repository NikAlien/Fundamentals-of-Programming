#
# This module is used to invoke the program's UI and start it. It should not contain a lot of code.
#
import ui
from src import functions


def start():
    contestant_list = functions.random_generator(10)
    ui.menu(contestant_list)


start()