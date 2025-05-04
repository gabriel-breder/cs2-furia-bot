from aiogram import types
from dotenv import load_dotenv
import requests
import os

load_dotenv()

API_URL = os.getenv('API_URL')

def get_results():
    response = requests.get(f"{API_URL}/matches_results/")
    return parse_matches(response)

def get_next_matches():
    response = requests.get(f"{API_URL}/next_matches/")
    return parse_matches(response)

def parse_matches(response):
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

async def get_matches_handler(message: types.Message):
    await message.answer("Carregando resultados...")

    matches = get_results()

    if not matches['matches']:
        await message.answer("Nenhum resultado encontrado.")
        return

    if matches is None:
        await message.answer("Erro ao carregar os resultados.")
        return
    
    response = "\n\n".join(
        f"{match['teamA']} {match['teamA_score']} vs {match['teamB_score']} {match['teamB']}\n"
        f"{match['tournament']}"
        for match in matches['matches']
    )

    await message.answer(response)

async def get_next_matches_handler(message: types.Message):
    await message.answer("Carregando próximas partidas...")

    matches = get_next_matches()
    
    if not matches['matches']:
        await message.answer("Nenhuma partida encontrada.")
        return

    if matches['matches'] is None:
        await message.answer("Erro ao carregar as próximas partidas.")
        return

    response = "\n\n".join(
        f"{match['teamA']} vs {match['teamB']}\n"
        f"{match['tournament']}"
        for match in matches['matches']
    )

    await message.answer(response)