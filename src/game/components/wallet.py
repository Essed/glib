from engine.wallet import Wallet

class PlayerWallet:
    def __init__(self) -> None:
        self.__wallet = Wallet(0)

    @property
    def wallet_obj(self):
        return self.__wallet
    
    async def balance(self):
        return await self.__wallet.get_balance()
    
    async def accure(self, value: float):
        amount = await self.balance() + value
        await self.__wallet.set_balance(amount)
    
    async def withdraw(self, value: float):
        amount = await self.balance() - value
        await self.__wallet.set_balance(amount)
    
