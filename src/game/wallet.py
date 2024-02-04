from game import player

class Wallet:
    def __init__(self, player: player.Player, amount: float) -> None:
        self.__player = player
        self.__amount = amount
        self.__coin = None

    def get_balance(self) -> float:
        return self.__amount

    def set_balance(self, amount: float):
        self.__amount = amount

    def get_coin(self) -> str:
        return self.__coin

    def set_coin(self, coin: str):
        self.__coin = coin
    
    def show(self):
        print(self.__player, self.__coin, self.__amount)