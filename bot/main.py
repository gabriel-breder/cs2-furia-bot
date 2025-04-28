from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from handlers.start import start_handler
from handlers.players import get_players_handler
from handlers.matches import get_matches_handler, get_next_matches_handler
from handlers.social import get_medias_handler
from handlers.news import get_news_handler
from handlers.fall_back import fallback_handler
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.message.register(start_handler, Command("start", "help"))
    dp.message.register(get_players_handler, Command("players"))
    dp.message.register(get_matches_handler, Command("resultados"))
    dp.message.register(get_next_matches_handler, Command("proximas"))
    dp.message.register(get_medias_handler, Command("social"))
    dp.message.register(get_news_handler, Command("noticias"))
    dp.message.register(fallback_handler)

    print("Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
