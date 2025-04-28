from aiogram import types

async def start_handler(message: types.Message):
    user = message.from_user

    response = (
        f"Olá, {user.first_name}!\n"
        "Use /players para ver a lista de jogadores da Furia\n"
        "Use /resultados para ver os resultados das últimas partidas\n"
        "Use /proximas para ver as próximas partidas\n"
        "Use /noticias para ver as últimas notícias\n"
        "Use /redes para ver as redes sociais da Furia\n"
    )

    await message.answer(response)
