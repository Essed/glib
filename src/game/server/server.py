from game.unitdb.unit_tools import Generator, Loader, StatsCompiler, UnitDatabase
from configparser import ConfigParser
from dataclasses import dataclass
import os 

@dataclass
class GeneratorSettings:
    stats_compiler: StatsCompiler = StatsCompiler(0, 0, 0, 0)

    def set_stats(self, hp_value, armor_value, damage_value, level_value):
        self.stats_compiler = StatsCompiler(hp_value, armor_value, damage_value, level_value)
    
@dataclass
class LoaderSettings:
    unit_database: UnitDatabase = UnitDatabase()


class ServerConfig:
    def __init__(self, config_path: str) -> None:
        self.__config = ConfigParser()
        self.__generator_settings = GeneratorSettings()
        self.__loader_settings = LoaderSettings()
        self.__config_path = config_path
        
    @property
    def generator_settings(self):
        return self.__generator_settings

    @property
    def loader_settings(self):
        return self.__loader_settings

    def __set_generator_settings(self, hp_value, armor_value, damage_value, level_value):
        self.__generator_settings.set_stats(hp_value, armor_value, damage_value, level_value)

    def generate_default(self):
        self.__set_configs()

    def generate(self):
        if not os.path.exists(self.__config_path):
            self.__set_generator_settings(100, 35, 25, 5)
            self.__set_configs()
            return
        
        stats = self.get_compiler()
        self.__set_generator_settings(stats.hp, stats.armor, stats.damage, stats.level)

    def __set_configs(self):        
        self.__config.add_section("StatsCompiler")
        self.__config.set("StatsCompiler", "hp", str(self.__generator_settings.stats_compiler.hp))
        self.__config.set("StatsCompiler", "armor", str(self.__generator_settings.stats_compiler.armor))
        self.__config.set("StatsCompiler", "level", str(self.__generator_settings.stats_compiler.level))
        self.__config.set("StatsCompiler", "damage", str(self.__generator_settings.stats_compiler.damage))

    def save_config(self):
        with open(self.__config_path, "w") as file:
            self.__config.write(file)

    def __get_config(self) -> dict:
        if not os.path.exists(self.__config_path):
            return 

        self.__config.read(self.__config_path)
        config = {            
            "StatsCompiler": {
                "hp": self.__config.get("StatsCompiler", "hp"), 
                "armor": self.__config.get("StatsCompiler", "armor"),
                "level": self.__config.get("StatsCompiler", "level"),
                "damage": self.__config.get("StatsCompiler", "damage")
            }
        }
        return config

    def get_compiler(self):
        stats = self.__get_config()["StatsCompiler"]
        for key, value in stats.items():
            stats[key] = int(value)
        stats_compiler = StatsCompiler(stats["hp"], stats["armor"], stats["damage"], stats["level"])
        return stats_compiler

    def make_generator(self):
        stats_compiler = self.get_compiler()
        return Generator(stats_compiler, self.__loader_settings.unit_database)
    
    def make_loader(self):
        return Loader(self.__loader_settings.unit_database)




class GameServer:
    def __init__(self, generator: Generator, loader: Loader) -> None:
        self.__generator = generator
        self.__loader = loader
        self.__logs = list()

    def awake(self, path_unit_db: str, units_amount: int):   
        print("Game server awake... ")     
        if not os.path.exists(path_unit_db):
            units = self.__generator.generate_units(units_amount)
            self.__generator.save_database(units, path_unit_db)
        
        units_db = self.__loader.load(path_unit_db)        
        print(units_db)

    def start(self):
        print("Game server start... ")

    