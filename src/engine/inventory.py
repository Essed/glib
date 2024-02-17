
class Inventory:
    def __init__(self) -> None:
        self.__inventory = dict()
        self.__items = dict()

    def get_inventory(self):
        return self.__inventory

    def get_items(self):
        return self.__items

    def add_item(self, item, amount: int):
        if not item in self.__inventory:
            self.__inventory[item] = amount
            self.__items[item] = False
    
    def acquire_item(self, item):
        if item in self.__items:
            self.__items[item] = True

    def unacquire_item(self, item):
        if item in self.__items:
            self.__items[item] = False

    def is_acquired(self, item) -> bool:
        return self.__items[item]

    def get_acquired_items(self):
        return [item for item in self.__items if self.__items[item]]

    def count_items(self) -> int:
        return len(self.__inventory)

    def show(self):
        print(self.__inventory, self.__items)