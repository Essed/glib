

class Player:
    
    def __init__(self, nickname) -> None:
        self.__nickname = nickname
    
    def get_player_nickname(self) -> str:
        return self.__nickname
    
    
    