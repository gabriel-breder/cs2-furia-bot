from aiogram import types
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

async def get_matches_handler(message: types.Message):
    await message.answer("Carregando resultados...")

    matches = get_results()

    if matches is None:
        await message.answer("Erro ao carregar os resultados.")
        return

    response = "\n\n".join(
        f"{replace_dots(match['teamA'])} {match['teamA_score']} vs {match['teamB_score']} {replace_dots(match['teamB'])}\n"
        f"{match['tournament']}"
        for match in matches['matches']
    )

    await message.answer(response, parse_mode="MarkdownV2")
