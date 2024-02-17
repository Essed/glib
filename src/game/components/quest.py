from engine.quest import Quest

class PlayerQuest:
    def __init__(self, name: str, award: float, duration_seconds: int, description: str, url: str = None) -> None:
        self.__quest = Quest(name, award, duration_seconds, description, url)

    @property
    def quest(self):
        return self.__quest
    
    def complete(self):
        self.__quest.complete()

    def is_complete(self) -> bool:
        return self.__quest.is_complete()
    
    def quest_name(self) -> str:
        return self.__quest.get_quest_name()

    def get_award(self):
        return self.__quest.get_award()
    
    def finish_time(self):
        return self.__quest.get_finish_time()
    
    def get_url(self) -> str:
        return self.__quest.get_quest_url()
    
    def get_description(self) -> str:
        return self.__quest.get_description()