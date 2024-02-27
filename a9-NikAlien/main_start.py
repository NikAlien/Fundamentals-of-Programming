from board_repo import GomokuBoard
from game_play_services import GameServices
from ui import UI


board = GomokuBoard()
services = GameServices(board)
ui = UI(services)

ui.start()