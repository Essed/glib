from game.unitdb.unit_tools import Generator, Loader, StatsCompiler, UnitDatabase
from game.gamelogic.game import Game
from game.components.player import Player
from game.components.dinosaur import Dinosaur
from game.database.db import DataBase

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
        
        self.__get_config()
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
        stats: dict = self.__get_config()["StatsCompiler"]
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
    def __init__(self, generator: Generator, loader: Loader, game: Game) -> None:
        self.__generator = generator
        self.__loader = loader
        self.__game = game
        self.__unit_database = None
        self.__players = list()
        self.__database = DataBase("C:/Users/vipar/OneDrive/Desktop/tgplay/game.db")

    @property
    def game(self):
        return self.__game
    
    @property
    def unit_database(self):
        return self.__unit_database


    async def __create_unit_database(self, unit_db: UnitDatabase):
        self.__unit_database = unit_db


    async def awake(self, path_unit_db: str, units_amount: int):   
        print("Game server awake...")     
        print("\tDatabase connected:", self.__database)
        
        if not os.path.exists(path_unit_db):
            units = await self.__generator.generate_units(units_amount)
            await self.__generator.save_database(units, path_unit_db)
        
        units_db = self.__loader.load(path_unit_db)
        await self.__create_unit_database(units_db)
        print("\tUnit Database created:", units_db)

    async def start(self):
        print("Game server start...")
        print("\tGame title:", self.__game.title)
        print("\tGame version:", self.__game.version)


    async def connect(self, player: Player):
        self.__players.append(player)
        print(f"\tPlayer '{await player.nickname()}' connected")


    async def instance_dino(self, index: int) -> Dinosaur:
        dino = await self.__unit_database.select_index(index)
        dino = await dino.unwrap()
        return Dinosaur(dino['name'], dino['race'], dino['level'], dino['attack_type'], dino['damage'], dino['rarity'], dino['armor'], dino['hp'])
    

    async def player_exists(self, nickname: str) -> bool:
        player = self.__database.get_user_by_nickname(nickname)

        if player is None:
            return False

        return True

    async def auth_player(self, player_id: str) -> bool:
        auth_status = self.__database.exist_user_with_id(player_id)

        print(auth_status)