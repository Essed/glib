from game.gamelogic.game import Game
from game.server.server import ServerConfig, GameServer
from game.server.action import Action, ActionRegistred, ActionLinker

if __name__ == "__main__":

    game = Game("Dinos")

    server_config = ServerConfig("game/server/config.ini")
    server_config.generate()
    server_config.save_config()

    game_server = GameServer(server_config.make_generator(), server_config.make_loader(), game)
    game_server.awake("game/unitdb/units.json", 10)
    game_server.start()

    ActionLinker(game_server)
    Action()
    ActionRegistred("Askme")