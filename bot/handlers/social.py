from aiogram import types
from dotenv import load_dotenv
import requests
import os

load_dotenv()

API_URL = os.getenv('API_URL')

def get_medias_from_api():
    response = requests.get(f"{API_URL}/social")

    if response.status_code == 200:
        medias = response.json()
        return medias
    else:
        print(f"Error: {response.status_code}")
        return None

async def get_medias_handler(message: types.Message):
    await message.answer("Carregando lista de jogadores...")
    medias = get_medias_from_api()

    if not medias:
        await message.answer("Nenhuma rede social encontrada.")
        return

    if medias is None:
        await message.answer("Erro ao carregar as redes sociais.")
        return

    response = "\n\n".join(
        f"{media['name']}: {media['link']}\n"
        for media in medias
    )

    await message.answer(response)
