from engine.actor import Actor

class Player:
    def __init__(self, nickname: str) -> None:
        self.__player = Actor(nickname)
        self.__inventory = None
        self.__balance  = None
        self.__quests = list()

    @property
    def player(self):
        return self.__player
    
    @property
    def inventory(self):
        return self.__inventory
    
    @property
    def balance(self):
        return self.__balance
    
    @property
    def quests(self):
        return self.__quests
    
    def nickname(self):
        return self.__player.get_nickname()

    def load_inventory(self, inventory):
        self.__inventory = inventory
    
    def change_balance(self, value: float):
        self.__balance = value

    def update_quests(self, quests: list):
        self.__quests = quests