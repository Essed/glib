from enum import Enum
from utils.enums import nameof
from random import randint
import json

class AttackType(Enum):
    MELEE = "Melee"
    RANGE = "Range"

class Race(Enum):
    ROCK = "Rock"
    SWAMPERS = "Swampers"

class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"


class StatsCompiler:
    def __init__(self, hp_value, armor_value, damage_value, level_value) -> None:
        self.__hp_value = hp_value
        self.__armor_value = armor_value
        self.__level_value = level_value
        self.__damage_value = damage_value

    @property
    def hp(self):
        return self.__hp_value

    @property
    def armor(self):
        return self.__armor_value
    
    @property
    def level(self):
        return self.__level_value
    
    @property
    def damage(self):
        return self.__damage_value

    def compile_stats(self):
        stats = dict()
        properties = self.prepare_properties().items()
        for property_name, property_value in properties:
            if type(property_value) == list:
                random_index = randint(0, len(property_value) - 1)
                stats[property_name] = property_value[random_index]
                continue
            stats[property_name] = property_value
        return stats

    def prepare_properties(self):
        properties = dict()
        
        attack_types = [attack_type for attack_type in AttackType]
        races = [race for race in Race]
        rarities = [rarity for rarity in Rarity]

        attack_type_classname = nameof(AttackType)
        race_classname = nameof(Race)
        rarity_classname = nameof(Rarity)

        hp_value = randint(1, self.__hp_value)
        armor_value = randint(1, self.__armor_value)
        level_value = randint(1, self.__level_value)
        damage_value = randint(1, self.__damage_value)


        properties[attack_type_classname] = attack_types
        properties[race_classname] = races
        properties[rarity_classname] = rarities
        properties["hp"] = hp_value
        properties["armor"] = armor_value
        properties["level"] = level_value
        properties['damage'] = damage_value

        return properties 



class Unit:
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

    def unwrap(self) -> dict:
        return {
            "name": self.__name,
            "race": self.__race.value,
            "level": self.__level,
            "attack_type": self.__attack_type.value,     
            "damage": self.__damage,
            "rarity": self.__rarity.value,
            "armor": self.__armor,
            "hp": self.__hp                   
        }

class UnitDatabase:
    def __init__(self) -> None:
        self.__units = list()

    @property
    def count(self):
        return len(self.__units)

    def add_unit(self, unit: Unit):
        self.__units.append(unit)

    def add_units(self, units: list[Unit]):
        self.__units.extend(units)

    def get_units(self):
        return self.__units

    def clear(self):
        self.__units.clear()

    def print_units(self):
        units_data = [unit.unwrap() for unit in self.__units]
        print(json.dumps(units_data, indent=4))

class UnitGenerator:
    def __init__(self, unit_db: UnitDatabase) -> None:
        self.__unit_db = unit_db
    
    def generate_unit(self) -> list[Unit]:
        unit_index = randint(0, len(self.__unit_db.get_units()) - 1)
        generated_unit = self.__unit_db.get_units()[unit_index]
        return generated_unit