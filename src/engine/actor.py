
class Actor:
    
    def __init__(self, nickname) -> None:
        self.__nickname = nickname
        self.__invites = list()

    def get_nickname(self) -> str:
        return self.__nickname
    
    def add_invite(self, invite):
        self.__invites.append(invite)
    