from engine.quest import Quest

class PlayerQuest:
    def __init__(self, name: str, award: float, duration_seconds: int, description: str, url: str = None) -> None:
        self.__quest = Quest(name, award, duration_seconds, description, url)

    @property
    def quest(self):
        return self.__quest
    
    async def complete(self):
        self.__quest.complete()

    async def is_complete(self) -> bool:
        return self.__quest.is_complete()
    
    async def quest_name(self) -> str:
        return self.__quest.get_quest_name()

    async def get_award(self):
        return self.__quest.get_award()
    
    async def finish_time(self):
        return self.__quest.get_finish_time()
    
    async def get_url(self) -> str:
        return self.__quest.get_quest_url()
    
    async def get_description(self) -> str:
        return self.__quest.get_description()