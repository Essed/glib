from dataclasses import dataclass
from engine.clan import Clan
from engine.actor import Actor
    

@dataclass
class ClanInvite:
    clan: Clan
    message: str
    addresser: Actor