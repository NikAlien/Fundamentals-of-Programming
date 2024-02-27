from src.repository import TextFileRepository
from src.services import Services
from src.ui import UI

player_list = TextFileRepository()
services = Services(player_list)

ui = UI(services)
ui.start()

