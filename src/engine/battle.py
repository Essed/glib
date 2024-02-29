from datetime import datetime, timedelta
from engine import unit

class Battle: 
    def __init__(self) -> None:
        self.__start_time = datetime.now()
        self.__units = list()

    async def show(self):
        print(self.__start_time)

    async def add_unit(self, unit):
        self.__units.append(unit)

    async def get_units(self) -> list[unit.Unit]:
        return self.__units

    async def get_start_time(self):
        return self.__start_time


class PVE(Battle):
    def __init__(self, time_seconds: float) -> None:
        super().__init__()
        self.__finish_time = None
        self.__time = time_seconds

    async def set_finish_time(self):
        self.__finish_time = await super().get_start_time() + timedelta(seconds=self.__time)
        
    async def get_finish_time(self):
        return self.__finish_time

    async def progress_unit(self, exp_value):
        for unt in self.get_units():
            unt.add_experience(exp_value)

    async def instance_unit(self, unit_db: unit.UnitDatabase):
        return unit.UnitGenerator(unit_db).generate_unit()
    
    async def finish(self):
        self.__finish_time = None
        self.__time = 0
        return self