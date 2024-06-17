import telebot

bot = telebot.TeleBot('7486383790:AAHKlMrGIKGuzcM_GpLtqVFVgf8CUHI_XGM')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Поздравляем, Вы были приняты на работу в нашу компанию!')


bot.polling(none_stop=True)