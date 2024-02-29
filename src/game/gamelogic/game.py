from game.components.player import Player
from game.components.inventory import PlayerInventory
from game.components.wallet import PlayerWallet 
from game.components.quest import PlayerQuest
from game.components.dinosaur import Dinosaur
from engine.battle import PVE



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

    async def registred_new_player(self, nickname: str):
        player = Player(nickname)
        return player

    async def create_default_account(self, player: Player) -> Player:
        await player.load_inventory(PlayerInventory())
        await player.change_balance(await PlayerWallet().balance())

        return player
    
    async def start_reward(self, player: Player, dino: Dinosaur, amount: int) -> Player:
        inventory = PlayerInventory()
        await inventory.add_item(dino, amount)
        await player.load_inventory(inventory)
        return player

    async def start_grind(self, player: Player, duration_seconds: float) -> PVE:
        pve = PVE(duration_seconds)
        dinos = await player.inventory.all_dinos()
        await pve.set_finish_time()
        await pve.get_finish_time()
        for dino in dinos:
            await pve.add_unit(dino)
        return pve
    
    async def spawn_boss(self, player: Player, boss: Dinosaur):
        await player.current_boss(boss)

    async def lock_dinos(self, player: Player) -> Player:
        await player.inventory.locked_item(player.inventory.all_dinos()[0])
        return player

    
    async def unlock_dinos(self, player: Player) -> Player:
        await player.inventory.unlocked_item(player.inventory.all_dinos()[0])
    

