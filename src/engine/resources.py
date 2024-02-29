

class Resource: 
    def __init__(self, max_quantity, quantity) -> None:
        self.__max_quantity = max_quantity
        self.__quantity = quantity
    
    async def _set_max_quantity(self, max_quantity):
        self.__max_quantity = max_quantity
    
    async def _set_quantity(self, quantity):
        self.__quantity = quantity

    async def get_max_quantity(self) -> int:
        return self.__max_quantity
    
    async def get_quantity(self) -> int:
        return self.__quantity
    
    async def equal_quantity(self):
        if self.__quantity > self.__max_quantity:
            self.__quantity = self.__max_quantity



class Energy(Resource):
    def consume(self, value):
        new_quantity = self.get_quantity() - value
        self._set_quantity(new_quantity)
    
    async def increase(self, value):
        if self.get_quantity() < self.get_max_quantity():
            new_quantity = self.get_quantity() + value
            self._set_quantity(new_quantity)
            self.equal_quantity()

    async def refresh(self):
        max_quantity = self.get_max_quantity()
        self._set_quantity(max_quantity)

    async def upgrade_max_energy(self, value):
        self._set_max_quantity(value)