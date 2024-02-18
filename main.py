import telebot
import data_base

bot = telebot.TeleBot("6780240670:AAFESmE0z3eRNfGWd5cnn-payG9tNmxhVWw")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, напиши свою группу в формате "/set_group 22-ПМ-1"')


@bot.message_handler(commands=['set_group'])
def set_group(message):
    data_base.add_user(message.from_user.first_name, message.from_user.username, message.chat.id, message.text[11:])


bot.polling(non_stop=True)