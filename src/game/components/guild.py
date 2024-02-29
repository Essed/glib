from engine.clan import Clan
from game.components.player import Player



class Guild():
    def __init__(self, name: str, tag: str, player: Player) -> None:
        self.__guild = Clan(name, tag, player.player)
        self.__rank = 1
        self.accept(player)

    @property
    def guild(self):
        return self.__guild

    @property
    def rank(self):
        return self.__rank

    async def tag(self) -> str:
        return self.__guild.get_tag()

    async def name(self) -> str:
        return self.__guild.get_name()
    
    async def leader(self) -> str:
        return self.__guild.get_clan_leader()
    
    async def rank_up(self, value: int):
        self.__rank += value

    async def level_up(self, value: int):
        return self.__guild.level_up(value)

    async def accept(self, player: Player):
        return self.__guild.accept(player.player)
    
    async def kick(self, nickname: str):
        return self.__guild.kick(nickname)

    async def appoint_leader(self, nickname: str):
        return self.__guild.set_leadership(nickname)
    
    async def members(self):
        members = [Player(await member.get_nickname()) for member in await self.__guild.get_members()]
        return members

    async def status(self):
        return self.__guild.status()

    async def members_nickname(self):
        return self.__guild.get_members_nickname()