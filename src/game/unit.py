from enum import Enum
from utils.enums import nameof
from random import randint

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



class StatsCompiler:
    def __init__(self, hp_value, armor_value, level_value) -> None:
        self.__hp_value = hp_value
        self.__armor_value = armor_value
        self.__level_value = level_value

    def compile_stats(self):
        stats = dict()
        properties = self.__prepare_properties().items()

        for property_name, property_value in properties:
            if type(property_value) == list:
                stats[property_name] = randint(0, len(property_value) - 1)
                print(property_name, property_value)
        print(stats)

        

    def __prepare_properties(self):
        properties = dict()
        
        attack_types = [attack_type for attack_type in AttackType]
        races = [race for race in Race]
        rarities = [rarity for rarity in Rarity]

        attack_type_classname = nameof(AttackType)
        race_classname = nameof(Race)
        rarity_classname = nameof(Rarity)

        hp_value = 0
        armor_value = 0
        level_value = 0

        properties[attack_type_classname] = attack_types
        properties[race_classname] = races
        properties[rarity_classname] = rarities
        properties["hp"] = hp_value
        properties["armor"] = armor_value
        properties["level"] = level_value

        return properties 




class Dinosaur:
    def __init__(self, name, 
                 race: Race, level: int, 
                 attack_type: AttackType, damage: float,
                 rarity: Rarity,
                 armor: float,
                 hp: float) -> None:
        
        self.__name = name
        self.__attack_type = attack_type
        self.__level = level
        self.__damage = damage
        self.__rarity = rarity
        self.__armor = armor
        self.__race = race
        self.__hp = hp
        self.__experience_for_up: int = 0
        self.__experience: int = 0
   
    def show(self):
        print(self.__name, self.__race.name,
              self.__attack_type.name, self.__level, self.__rarity.name,
              self.__damage, self.__armor, self.__hp,
              self.__experience, self.__experience_for_up
            )

    def apply_damage(self, damage: float):
        self.__hp -= damage

    def add_experience(self, exp_value: int):
        self.__experience += exp_value
    
    def try_levelup(self) -> bool:
        if self.__experience_for_up != self.__experience:
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
