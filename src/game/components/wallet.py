from engine.wallet import Wallet

class PlayerWallet:
    def __init__(self) -> None:
        self.__wallet = Wallet(0)

    @property
    def wallet_obj(self):
        return self.__wallet
    
    def balance(self):
        return self.__wallet.get_balance()
    
    def accure(self, value: float):
        amount = self.balance() + value
        self.__wallet.set_balance(amount)
    
    def withdraw(self, value: float):
        amount = self.balance() - value
        self.__wallet.set_balance(amount)
    
