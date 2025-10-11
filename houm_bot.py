import telebot
import random
from bot_logic import gen_pass, gen_emodji, flip_cube, get_duck_image_url
import os


bot = telebot.TeleBot("7557234987:AAEPYBFDmfncr2gEVD4oWF1oTC0Yn0Ymk8A")  # Не забудьте заменить на ваш токен

images = ['images\5ea4791c-aa9f-4a48-b6c2-4968d0addab7.jpeg',
          'images\7b9821e2-c6df-4734-98ec-9fa2c6d6f0b7.jpeg',
          '\images\81f63572-0ddb-4ba2-acde-9e2b8f52d389.jpeg']



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['par'])
def send_pass(message):
    bot.reply_to(message, gen_pass(10))

@bot.message_handler(commands=['cube'])
def send_cube(message):
    dice_result = bot.send_dice(message.chat.id, emoji='⚽')
    bot.reply_to(message, f"Кубик выпал на {dice_result.dice.value}")

@bot.message_handler(commands=['mem'])
def send_mem(message):
    with open(random.choice(images), 'rb') as f:
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['emo'])
def send_emo(message):
    bot.reply_to(message, gen_emodji())

@bot.message_handler(commands=['duck'])
def send_duck(message):
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

bot.polling()
