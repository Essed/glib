from game.server.server import GameServer
from game.gamelogic.game import Game

class GameAPI():
    def __init__(self, game_server: GameServer) -> None:
        self.__server = game_server 
        self.__game = game_server.game

    def api_info(self):
        print(self.__server, self.__game)