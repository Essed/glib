from game.server.server_packet import Packet
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
        self._packet = Packet()
        self._send_packet()

    def _send_packet(self):
        self._packet.load_data(self)
        self._server.perform_action(self._packet)

    def perform(self):
        return {
            "Action": self
        }




class ActionRegister(Action):
    def __init__(self, nickname: str) -> None:
        self.__nickname = nickname
        super().__init__()


    def _send_packet(self):        
        self._packet.load_data(self)
        return super()._send_packet()
        
    def perform(self):
        player = self._game.registred_new_player(self.__nickname)
        result = {
            "Action": self,
            "player": player,
        }
        return result