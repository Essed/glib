

class Resource: 
    def __init__(self, max_quantity, quantity) -> None:
        self.__max_quantity = max_quantity
        self.__quantity = quantity
    
    def _set_max_quantity(self, max_quantity):
        self.__max_quantity = max_quantity
    
    def _set_quantity(self, quantity):
        self.__quantity = quantity

    def get_max_quantity(self) -> int:
        return self.__max_quantity
    
    def get_quantity(self) -> int:
        return self.__quantity
    
    def equal_quantity(self):
        if self.__quantity > self.__max_quantity:
            self.__quantity = self.__max_quantity



class Energy(Resource):
    def consume(self, value):
        new_quantity = self.get_quantity() - value
        self._set_quantity(new_quantity)
    
    def increase(self, value):
        if self.get_quantity() < self.get_max_quantity():
            new_quantity = self.get_quantity() + value
            self._set_quantity(new_quantity)
            self.equal_quantity()

    def refresh(self):
        max_quantity = self.get_max_quantity()
        self._set_quantity(max_quantity)

    def upgrade_max_energy(self, value):
        self._set_max_quantity(value)