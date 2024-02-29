
class Wallet:
    def __init__(self, amount: float) -> None:
        self.__amount = amount
        self.__coin = None

    async def get_balance(self) -> float:
        return self.__amount

    async def set_balance(self, amount: float):
        self.__amount = amount

    async def get_coin(self) -> str:
        return self.__coin

    async def set_coin(self, coin: str):
        self.__coin = coin
    
    async def show(self):
        print(self.__coin, self.__amount)