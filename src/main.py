from game.components.player import Player
from game.components.guild import Guild
from game.components.inventory import PlayerInventory
from game.components.wallet import PlayerWallet
from game.gamelogic.game import Game
from game.unitdb.unit_tools import Generator, Loader, StatsCompiler, UnitDatabase
from game.server.server import ServerConfig

if __name__ == "__main__":
    gm1 = Game()
    player1 = gm1.registred_new_player("Askme")
    gm1.create_default_account(player1)
    print(player1, player1.inventory, player1.balance, player1.quests)
    gen = Generator(StatsCompiler(100, 35, 25, 5), UnitDatabase())
    units = gen.generate_units(10)
    gen.save_database(units, "game/unitdb/units.json")


    unit_db = UnitDatabase() 
    lod = Loader(unit_db)
    data = lod.load("game/unitdb/units.json")
    
    for dat in data:
        dat.show()

    server_config = ServerConfig("game/server/config.ini")
    server_config.generate_default()
    server_config.save_config()
    #cfg = server_config.get_config()
    #print(cfg)
    #print(server_config.generator)
    #print(server_config.loader)