from engine.unit import AttackType, Race, Rarity, Unit

class Dinosaur(Unit):
    def __init__(self, name: str, race: Race, level: int, attack_type: AttackType, damage: float, rarity: Rarity, armor: float, hp: float) -> None:
        self.__name = name
        self.__race = race
        self.__level = level
        self.__attack_type = attack_type
        self.__damage = damage
        self.__rarity = rarity
        self.__armor = armor
        self.__hp = hp

    async def unwrap(self) -> dict:
        return {
            "name": self.__name,
            "race": self.__race,
            "level": self.__level,
            "attack_type": self.__attack_type,
            "damage": self.__damage,
            "rarity": self.__rarity,
            "armor": self.__armor,
            "hp": self.__hp
        }