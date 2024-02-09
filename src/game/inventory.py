
class Inventory:
    def __init__(self) -> None:
        self.__inventory = dict()
        self.__items = dict()

    def add_item(self, item, amount: int):
        if not item in self.__inventory:
            self.__inventory[item] = amount
            self.__items[item] = True
    
    def acquire_item(self, item) -> bool:
        if item in self.__items:
            self.__items[item] = False
            return True
        return False

    def count_items(self) -> int:
        return len(self.__inventory)

    def show(self):
        print(self.__inventory, self.__items)