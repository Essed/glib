
class Actor:
    
    def __init__(self, nickname) -> None:
        self.__nickname = nickname
        self.__invites = list()

    async def get_nickname(self) -> str:
        return self.__nickname
    
    async def add_invite(self, invite):
        self.__invites.append(invite)
    