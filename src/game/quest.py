


class Quest:
    def __init__(self, quest_name: str, award_amount: int) -> None:
        self.__status = False
        self.__quest_name = quest_name
        self.__award_amount = award_amount
    
    def complete(self):
        self.__status = True
    
    def is_complete(self):
        return self.__status
    
    def get_quest_name(self):
        return self.__quest_name
    
    def get_award(self):
        return self.__award_amount
    
    