import telebot
import requests
import json
from config import TOKEN
from extentions import *


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def description(message):
    bot.send_message(message.chat.id, 'Для использования бота введите ссобщение в формате\nвалюта1 валюта2 количество\n'
                                      'бот переведет (количество) валюты1 в валюту2\n'
                                      'введите /value чтобы увидеть доступные валюты')


@bot.message_handler(commands=['value'])
def description(message):
    bot.send_message(message.chat.id, 'доступные валюты: биткоин, доллар, эфириум')


@bot.message_handler(content_types=['text'])
def convert(message):
    try:
        fsym, tsyms, amount = message.text.split(' ')
        if fsym == tsyms:
            raise ValueError
        text = CryptoConverter.convertion(fsym, tsyms, amount)
        bot.send_message(message.chat.id, f'{amount} {fsym} - {text} {tsyms}')
    except ValueError:
        bot.send_message(message.chat.id, 'Ошибка: Параметры указаны неверно\n'
                                          'Чтобы получить инструкци к боту введите /start или /help')
    except KeyError:
        bot.send_message(message.chat.id, 'Ошибка: Введена неверная валюта\n'
                                          'Чтобы получить список валют введите /value')


bot.polling(non_stop=True)
