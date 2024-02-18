from engine.invite import ClanInvite
from game.components.guild import Guild
from game.components.player import Player
from dataclasses import dataclass

@dataclass
class GuildInvite:
    guild: Guild
    addresser: Player
    message: str

    
    def base(self):
        return ClanInvite(self.guild.guild, self.message, self.addresser.player)
