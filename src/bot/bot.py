import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from hanlders.user_private import user_private_router


token = "6707067426:AAETn7RXgbp8QQRjLsnrR10biuQdl1P2LvQ"

bot = Bot(token=token)
dp = Dispatcher()

dp.include_router(user_private_router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())