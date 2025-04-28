from aiogram import types
from dotenv import load_dotenv
import requests
import os

load_dotenv()

API_URL = os.getenv('API_URL')

def get_news_from_api():
    response = requests.get(f"{API_URL}/news/")

    if response.status_code == 200:
        news = response.json()
        return news
    else:
        print(f"Error: {response.status_code}")
        return None

async def get_news_handler(message: types.Message):
    news = get_news_from_api()

    if not news:
        await message.answer("Nenhum jogador encontrado.")
        return

    if news is None:
        await message.answer("Erro ao carregar a lista de jogadores.")
        return

    response = "\n\n".join(
        f"{n['title']} {n['date']}\n{n['link']}"
        for n in news
    )

    await message.answer(response)
