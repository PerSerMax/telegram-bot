import telebot
import telegram

import data_base

bot = telebot.TeleBot("6780240670:AAFESmE0z3eRNfGWd5cnn-payG9tNmxhVWw")


@bot.message_handler(commands=['start'])
def start(message: telegram.Message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}, напиши /help, чтобы посмотреть все команды')


@bot.message_handler(commands=['help'])
def help(message: telegram.Message):
    bot.send_message(message.chat.id, "/set_group [ваша группа] - чтобы поменять/задать группу\n"
                                      "/set_schedule [ДЕНЬ] [НОМЕР ПАРЫ] [ВРЕМЯ НАЧАЛА ПАРЫ] [АУДИТОРИЯ] [НАЗВАНИЕ ПАРЫ] [ИМЯ ПРЕПОДА] - поменять конкретную пару")


@bot.message_handler(commands=['set_schedule'])
def set_schedule(message: telegram.Message):
    row = [] * 6
    if len(message.text.split()) == 7:
        row = message.text[13:].rstrip().lstrip().split(maxsplit=6)
        print(data_base.find_group(message.from_user.username),
                               row[0], row[1], row[2], row[3], row[4], row[5])
        data_base.set_schedule(data_base.find_group(message.from_user.username),
                               row[0], row[1], row[2], row[3], row[4], row[5])


@bot.message_handler(commands=['set_group'])
def set_group(message: telegram.Message):
    if len(message.text.rstrip().split()) > 1:
        data_base.add_user(message.from_user.username, message.chat.id, message.text[11:])


while True:
    bot.polling()