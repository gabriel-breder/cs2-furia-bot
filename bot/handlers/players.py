from telebot.types import Message
from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()

API_URL = os.getenv('API_URL')

def get_players_from_api():
    response = requests.get(f"{API_URL}/players")

    if response.status_code == 200:
        players = response.json()
        return players
    else:
        print(f"Error: {response.status_code}")
        return None
    

def get_players_handler(bot):
    
    def get_players(message: Message):
        players = get_players_from_api()
        
        response = "\n\n".join(
            f"Nome: {player['nickname']} \n Instagram: {player['social_media']['instagram']}\n Twitch: {player['social_media']['twitch']}\n"
            for player in players
        )
        bot.send_message(message.chat.id, response)
    return get_players