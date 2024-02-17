from datetime import datetime, timedelta

class Quest:
    def __init__(self, quest_name: str, award_amount: float,
                  duration_seconds: int, description: str, url: str = None) -> None:
        self.__status = False
        self.__quest_name = quest_name
        self.__award_amount = award_amount
        self.__duration_second = duration_seconds       
        self.__description = description
        self.__url = url
        self.__created_time = datetime.now()
    
    def complete(self):
        self.__status = True
    
    def is_complete(self):
        return self.__status
    
    def get_quest_name(self):
        return self.__quest_name
    
    def get_award(self):
        return self.__award_amount
        
    def get_finish_time(self):
        return self.__created_time + timedelta(seconds=self.__duration_second)
    
    def get_quest_url(self):
        return self.__url
    
    def get_description(self):
        return self.__description
