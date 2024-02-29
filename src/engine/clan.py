from engine import actor
from typing import List



class Clan:
    def __init__(self, name: str, clan_tag: str, clan_leader: actor.Actor) -> None:
        self.__name = name
        self.__clan_tag = clan_tag
        self.__members = dict()
        self.__level = 1
        self.__clan_leader = clan_leader

    async def level_up(self, value):
        self.__level+=value

    async def invite(self, actor: actor.Actor):
        pass

    async def accept(self, actor: actor.Actor):
        self.__members[actor] = actor.get_nickname()

    async def __find_member_by_nickname(self, nickname: str) -> actor.Actor:
        actor = [member for member in self.__members.keys() if member.get_nickname() == nickname].pop()
        return actor

    async def kick(self, nickname: str):
        member = self.__find_member_by_nickname(nickname)
        self.__members.pop(member)
    
    async def set_leadership(self, nickname: str):
        member = self.__find_member_by_nickname(nickname)
        self.__clan_leader = member

    async def get_members(self) -> List[actor.Actor]:
        return list(self.__members.keys())
    
    async def get_members_nickname(self):
        return list(member for member in self.__members.values())
    
    async def get_clan_leader(self) -> str:
        return self.__clan_leader.get_nickname()
    
    async def get_name(self):
        return self.__name
    
    async def get_tag(self):
        return self.__clan_tag


    async def status(self):
        return dict({
            "Name": self.__name,
            "Tag": self.__clan_tag,
            "Level": self.__level,
            "Leader":  self.__clan_leader.get_nickname()
        })
