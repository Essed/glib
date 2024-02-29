from game.server.server import GameServer, ServerConfig
from game.gamelogic.launcher import GameLauncher


from game.components.player import Player
from game.components.inventory import PlayerInventory

from game.gamelogic.game import Game


import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from bot.hanlders.user_private import user_private_router


token = "6707067426:AAETn7RXgbp8QQRjLsnrR10biuQdl1P2LvQ"

bot = Bot(token=token)
dp = Dispatcher()

dp.include_router(user_private_router)


def configure() -> ServerConfig:
    server_config = ServerConfig("game/server/config.ini")
    server_config.generate()
    server_config.save_config()

    return server_config


async def server_start(server_config: ServerConfig):    

    game_server = GameServer(server_config.make_generator(), server_config.make_loader(), Game("Dinos"))                
    await game_server.awake("game/unitdb/units.json", 10)
    await game_server.start()

    GameLauncher.game_server = game_server


async def main():        
    
    await server_start(configure())

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)




if __name__ == "__main__":
    asyncio.run(main())