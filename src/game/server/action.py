from game.server.server import GameServer


class ActionLinker:
    game_server = None
    def __init__(self, game_server: GameServer) -> None:
        ActionLinker.game_server: GameServer = game_server


class Action:
    def __init__(self) -> None:
        self.__server: GameServer = ActionLinker.game_server
        self.__perform()

    def __perform(self):
       self.__server.perform_action()