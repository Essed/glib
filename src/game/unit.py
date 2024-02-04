from enum import Enum

class AttackType(Enum):
    MELEE = "MELEE"
    RANGE = "RANGE"

class Race(Enum):
    ROCK = "Rock"
    SWAMPERS = "Swampers"

class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"

class Dinosaur:
    def __init__(self, name, 
                 race: Race, level: int, 
                 attack_type: AttackType, damage: float,
                 rarity: Rarity,
                 armor: float,
                 hp: float,) -> None:
        
        self.__name = name
        self.__attack_type = attack_type
        self.__level = level
        self.__damage = damage
        self.__rarity = rarity
        self.__armor = armor
        self.__race = race
        self.__hp = hp
        self.__experience_for_up: int = 0
        self.__experince: int = 0

    def show(self):
        print(self.__name, self.__race.name,
              self.__attack_type.name, self.__level, self.__rarity.name,
              self.__damage, self.__armor, self.__hp,
              self.__experince, self.__experience_for_up
            )

    def apply_damage(self, damage: float):
        self.__hp -= damage

    def add_experience(self, exp_value: int):
        self.__experince += exp_value
    
    def try_levelup(self) -> bool:
        if self.__experience_for_up != self.__experince:
            return False
        return True
    
    def level_up(self):
        self.__level += 1
    
    def reset_experience(self):
        self.__experince = 0
    
    def shift_experience(self):
        if self.__experince > self.__experience_for_up:   
            self.__experince = self.__experince - self.__experience_for_up
        
    def set_experience_for_up(self, exp_value: int):
        self.__experience_for_up = exp_value