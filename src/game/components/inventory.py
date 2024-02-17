from engine.inventory import Inventory


class PlayerInventory:
    def __init__(self) -> None:
        self.__inventory = Inventory()
    
    @property
    def inventory_obj(self):
        return self.__inventory
    
    @property
    def count_items(self):
        return self.__inventory.count_items()

    def inventory(self):
        return self.__inventory.get_inventory()
    
    def items_state(self):
        return self.__inventory.get_items()

    def add_item(self, item, value: int):
        self.__inventory.add_item(item, value)

    def locked_item(self, item):
        self.__inventory.acquire_item(item)

    def unlocked_item(self, item):
        self.__inventory.unacquire_item(item)

    def is_locked(self, item) -> bool:
        return self.__inventory.is_acquired(item)
    
