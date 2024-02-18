from game.components.player import Player
from game.components.inventory import PlayerInventory
from game.components.wallet import PlayerWallet 
from game.components.quest import PlayerQuest

class Game:
    def __init__(self, title: str) -> None:
        self.__title = title
        self.__version = "1.0"

    @property
    def title(self):
        return self.__title

    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    def registred_new_player(self, nickname: str):
        player = Player(nickname)
        return player

    def create_default_account(self, player: Player):
        player.load_inventory(PlayerInventory())
        player.change_balance(PlayerWallet().balance())
    
    