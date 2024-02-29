class Coin:

    def __init__(self, name: str) -> None:
        self.__name = name
    
    async def get_name(self) -> str:
        return self.__name