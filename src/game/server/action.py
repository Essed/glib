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
        self._logic = None
        self._params = dict()
        self._result = "result"
        self._perform({"Action": self, "params": self._params, "logic": self._logic})
    
    def _perform(self, data):
       self._server.perform_action(data)


class ActionRegister(Action):
    def __init__(self, nickname: str) -> None:
        self.__nickname = nickname
        super().__init__()

    def _perform(self, data):        
        self._params["nickname"] = self.__nickname
        self._logic = self._game.registred_new_player
        data = {
            "Action": self,
            "params": self._params,
            "logic": self._logic
        }
        return super()._perform(data)


