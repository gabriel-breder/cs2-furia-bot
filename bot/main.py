import os
from dotenv import load_dotenv
import telebot
from handlers.start import start_handler
from handlers.players import get_players_handler
from handlers.matches import get_matches_handler

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

def register_handlers():
    bot.register_message_handler(start_handler(bot), commands=['start'])
    bot.register_message_handler(get_players_handler(bot), commands=['players'])
    bot.register_message_handler(get_matches_handler(bot), commands=['matches'])

register_handlers()

def run_bot():
    print("Bot is running...")
    bot.infinity_polling()

run_bot()