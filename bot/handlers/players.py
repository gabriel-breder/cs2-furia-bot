from aiogram import types
from dotenv import load_dotenv
import requests
import os

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

async def get_players_handler(message: types.Message):
    await message.answer("Carregando lista de jogadores...")
    players = get_players_from_api()

    if not players:
        await message.answer("Nenhum jogador encontrado.")
        return

    if players is None:
        await message.answer("Erro ao carregar a lista de jogadores.")
        return

    response = "\n\n".join(
        f"{player['nickname']}\nInstagram: {player['social_media']['instagram']}\nTwitch: {player['social_media']['twitch']}"
        for player in players
    )

    await message.answer(response)
