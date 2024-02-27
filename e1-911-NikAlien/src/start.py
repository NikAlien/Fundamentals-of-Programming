from src.board_repo import GameBoard
from src.play_services import GameServices
from src.ui import UI

board = GameBoard()
services = GameServices(board)
ui = UI(services)

ui.start()


