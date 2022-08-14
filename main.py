import telebot
from telebot import types


bot = telebot.TeleBot('5443592273:AAG6X8T1fyuxuSap3qHwoeqfymy1b1yT1sk')


USER_DB = {}
def put_username(chatID, name):
    userInstance = USER_DB.get(chatID, {})
    userInstance['name'] = name
    USER_DB[chatID] = userInstance



@bot.message_handler(commands=['start'])
def str_name(message):
    msg = bot.send_message(message.chat.id, "What is you name?")
    put_username(msg.chat.id, msg.text)
    bot.register_next_step_handler(msg, str_last_name)

def str_last_name(message):
    msg = bot.send_message(message.chat.id, "What is you last name?")
    put_username(msg.chat.id, msg.text)
    bot.register_next_step_handler(msg, str_HB)

def str_HB(message):
    msg = bot.send_message(message.chat.id, "How old are you?")
    put_username(msg.chat.id, msg.text)
    bot.register_next_step_handler(msg, print_info)

def print_info(message):
    bot.send_message(message.chat.id, f'info')


bot.polling()




