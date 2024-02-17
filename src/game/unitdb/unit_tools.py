from engine.unit import Unit, StatsCompiler, UnitDatabase, Race, Rarity, AttackType
import json


class Generator:
    def __init__(self, compiler: StatsCompiler, unit_db: UnitDatabase) -> None:
        self.__compiler = compiler
        self.__unit_database = unit_db
    
    def generate_units(self, amount: int) -> list[Unit]:
        units = list()
        count = 0
        while count < amount:
            stats = self.__compiler.compile_stats()
            new_unit = Unit("Razor", stats['Race'], stats['level'], stats['AttackType'], stats['damage'], stats['Rarity'], stats['armor'], stats['hp'])
            self.__unit_database.add_unit(new_unit)
            units.append(new_unit.unwrap())
            count+=1
        return units
    
    def save_database(self, data, path: str):
        with open(path, 'w') as file:
            json.dump(data, file)


class Loader:
    def __init__(self, unit_db: UnitDatabase) -> None:
        self.__unit_database = unit_db
    
    def build_unit(self, data: dict) -> Unit:
        unit_name = data['name']
        unit_race = Race(data['race'])
        unit_level = data['level']
        unit_attack_type = AttackType(data['attack_type'])
        unit_damage = data['damage']
        unit_rarity = Rarity(data['rarity'])
        unit_armor = data['armor']
        unit_hp = data['hp']

        builded_unit = Unit(unit_name, unit_race, unit_level, unit_attack_type, unit_damage, unit_rarity, unit_armor, unit_hp)
        return builded_unit

    def load(self, path: str) -> list[Unit]:
        with open(path, 'r') as file:
            data = json.load(file)
            for element in data:
                loaded_unit = self.build_unit(element)
                self.__unit_database.add_unit(loaded_unit)            
        return self.__unit_database.get_units()