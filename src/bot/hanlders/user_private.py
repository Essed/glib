from aiogram import types, Router
from aiogram.filters import CommandStart, Command
from game.gamelogic.launcher import GameLauncher


user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(text="start")


@user_private_router.message(Command("register"))
async def registred_player(message: types.Message):
    
    game_server = GameLauncher.game_server

    if await game_server.player_exists(message.text) == True:
        await message.answer(text="Никнейм уже занят")
        return
    

    game = GameLauncher.game_server.game

    player = await game.registred_new_player(message.text)
    player = await game.create_default_account(player)
    await message.answer(text=f"Добро пожаловать в {game.title} {await player.nickname()}")



@user_private_router.message(Command("pve"))
async def grind(message: types.Message):
    
    game = GameLauncher.game_server.game
    
    player = await game.registred_new_player("askme")

    dino = await GameLauncher.game_server.instance_dino(0)

    await game.spawn_boss(player, dino)

    await message.answer(text=f"{player.__dict__}")



@user_private_router.message()
async def echo(message: types.Message):
    await message.answer(text=message.text)

