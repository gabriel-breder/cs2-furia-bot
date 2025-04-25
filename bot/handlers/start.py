from telebot.types import Message

def start_handler(bot):

    def response(first_name):
       return f"Olá, {first_name}! \n Use /players para ver a lista de jogadores da Furia \n Use /matches para ver os resultados das últimas partidas"

    def start(message: Message):
        user = message.from_user
        bot.send_message(message.chat.id, response(user.first_name))
    return start