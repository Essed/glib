from engine.inventory import Inventory
from game.components.dinosaur import Dinosaur

class PlayerInventory:
    def __init__(self) -> None:
        self.__inventory = Inventory()
    
    @property
    def inventory_obj(self):
        return self.__inventory
    
    @property
    def count_items(self):
        return self.__inventory.count_items()

    async def inventory(self):
        return await self.__inventory.get_inventory()
    
    async def all_dinos(self) -> list[Dinosaur]:
        items_in_inventory = await self.inventory()
        return [dino for dino in items_in_inventory if type(dino) == Dinosaur]

    async def items_state(self):
        return self.__inventory.get_items()

    async def add_item(self, item, value: int):
        await self.__inventory.add_item(item, value)

    async def locked_item(self, item):
        await self.__inventory.acquire_item(item)

    async def unlocked_item(self, item):
        await self.__inventory.unacquire_item(item)

    async def is_locked(self, item) -> bool:
        return self.__inventory.is_acquired(item)
    
