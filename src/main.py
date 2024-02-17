from game.components.player import Player
from game.components.guild import Guild
from game.components.inventory import PlayerInventory
from game.components.wallet import PlayerWallet
from game.gamelogic.game import Game
from game.unitdb.unit_tools import Loader, UnitDatabase
from game.server.server import ServerConfig, GameServer

if __name__ == "__main__":
    gm1 = Game()
    player1 = gm1.registred_new_player("Askme")
    gm1.create_default_account(player1)
    print(player1, player1.inventory, player1.balance, player1.quests)
    
    server_config = ServerConfig("game/server/config.ini")
    server_config.generate()
    server_config.save_config()
    generator = server_config.make_generator()

    game_server = GameServer(server_config.make_generator(), server_config.make_loader())

    game_server.awake("game/unitdb/units.json", 10)
    game_server.start()