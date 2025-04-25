from telebot.types import Message
from dotenv import load_dotenv
import requests
import os

load_dotenv()

API_URL = os.getenv('API_URL')

def replace_dots(text):
    return text.replace('.', ' ')

def get_results():
    response = requests.get(f"{API_URL}/get_matches_results/")

    if response.status_code == 200:
        matches = response.json()
        return matches
    else:
        print(f"Error: {response.status_code}")
        return None

def get_matches_handler(bot):
    
    def get_prev_matches_results(message: Message):
        chat_id = message.chat.id
        bot.send_message(chat_id, "Carregando resultados...")

        matches = get_results()

        response = "\n\n".join(
            f"{replace_dots(match['teamA'])} vs {replace_dots(match['teamB'])}\n"
            f"{match['teamA_score']} x {match['teamB_score']}\n"
            f"{match['tournament']}"
            for match in matches['matches']
        )

        bot.send_message(chat_id, response, parse_mode="MarkdownV2")
    return get_prev_matches_results