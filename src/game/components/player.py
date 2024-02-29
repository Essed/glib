from engine.actor import Actor
from game.components.inventory import PlayerInventory
from game.components.quest import PlayerQuest
from game.components.dinosaur import Dinosaur

class Player:
    def __init__(self, nickname: str) -> None:
        self.__player = Actor(nickname)
        self.__inventory = None
        self.__balance  = 0.0
        self.__quests = list()
        self.__boss = None

    @property
    def player(self):
        return self.__player
    
    @property
    def inventory(self) -> PlayerInventory:
        return self.__inventory
    
    @property
    def balance(self) -> float:
        return self.__balance
    
    @property
    def quests(self) -> list[PlayerQuest]:
        return self.__quests
    
    @property
    def boss(self) -> Dinosaur:
        return self.__boss

    async def nickname(self):
        return await self.__player.get_nickname()

    async def load_inventory(self, inventory):
        self.__inventory = inventory
    
    async def change_balance(self, value: float):
        self.__balance = value

    async def update_quests(self, quests: list):
        self.__quests = quests
    
    async def current_boss(self, boss: Dinosaur):
        self.__boss = boss