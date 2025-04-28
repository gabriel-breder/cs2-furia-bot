from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from handlers.start import start_handler
from handlers.players import get_players_handler
from handlers.matches import get_matches_handler
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Registrar Handlers usando filtros!
    dp.message.register(start_handler, Command("start"))
    dp.message.register(get_players_handler, Command("players"))
    dp.message.register(get_matches_handler, Command("matches"))

    print("Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
