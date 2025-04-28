from aiogram import types

async def fallback_handler(message: types.Message):
    await message.answer("Digite /help para ver a lista de comandos.")
