from game.server.server import GameServer
from game.gamelogic.game import Game

class ActionLinker:
    game_server = None
    def __init__(self, game_server: GameServer) -> None:
        ActionLinker.game_server: GameServer = game_server


class Action:
    def __init__(self) -> None:
        self._server: GameServer = ActionLinker.game_server
        self._game: Game = ActionLinker.game_server.game
        self._perform()
    
    def _perform(self):
       self._server.perform_action(self)    


class ActionRegistred(Action):
    def __init__(self, nickname: str) -> None:
        self.__nickname = nickname        
        super().__init__()

