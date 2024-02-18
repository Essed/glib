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

    def tag(self) -> str:
        return self.__guild.get_tag()

    def name(self) -> str:
        return self.__guild.get_name()
    
    def leader(self) -> str:
        return self.__guild.get_clan_leader()
    
    def rank_up(self, value: int):
        self.__rank += value

    def level_up(self, value: int):
        return self.__guild.level_up(value)

    def accept(self, player: Player):
        return self.__guild.accept(player.player)
    
    def kick(self, nickname: str):
        return self.__guild.kick(nickname)

    def appoint_leader(self, nickname: str):
        return self.__guild.set_leadership(nickname)
    
    def members(self):
        members = [Player(member.get_nickname()) for member in self.__guild.get_members()]
        return members

    def status(self):
        return self.__guild.status()

    def members_nickname(self):
        return self.__guild.get_members_nickname()