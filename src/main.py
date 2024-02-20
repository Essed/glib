from game.server.server import GameServer, ServerConfig

from game.components.player import Player
from game.components.inventory import PlayerInventory

from game.gamelogic.game import Game

if __name__ == "__main__":

    game = Game("Dinos")

    server_config = ServerConfig("game/server/config.ini")
    server_config.generate()
    server_config.save_config()

    game_server = GameServer(server_config.make_generator(), server_config.make_loader(), game)
    game_server.awake("game/unitdb/units.json", 10)
    game_server.start()