from aiogram import types

async def start_handler(message: types.Message):
    user = message.from_user

    response = (
        f"Olá, {user.first_name}!\n"
        "Use /players para ver a lista de jogadores da Furia\n"
        "Use /matches para ver os resultados das últimas partidas\n"
        "Use /help para ver os comandos disponíveis"
    )

    await message.answer(response)
