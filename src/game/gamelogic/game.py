from game.components.player import Player
from game.components.inventory import PlayerInventory
from game.components.wallet import PlayerWallet 
from game.components.quest import PlayerQuest

class Game:
    def __init__(self) -> None:
        pass

    def registred_new_player(self, nickname: str):
        player = Player(nickname)
        return player

    def create_default_account(self, player: Player):
        player.load_inventory(PlayerInventory())
        player.change_balance(PlayerWallet().balance())
    
    