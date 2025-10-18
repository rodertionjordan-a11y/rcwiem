import telebot
import random
from second_logic import gen_emodji,  get_sport_image_url
import os
import asyncio


bot = telebot.TeleBot("8403414525:AAFbOzzVVB-S2gS8m4xdaP_jMjmmoZA5kcY")  # Не забудьте заменить на ваш токен

images = [r'C:\Users\User\Python\t_bot\images\mem.jpeg',
          r'C:\Users\User\Python\t_bot\images\mem2.jpeg',
          r'C:\Users\User\Python\t_bot\images\mem3.jpeg']



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я - твой Telegram бот Олег. Если нужна помощь со спортом - я всегда у тебя в списке!")

@bot.message_handler(commands=['help'])
def send_hello(message):
    bot.reply_to(message, """
 /start - запуск бота
 /cube - бросок кубика
 /ball - пнуть мяч
 /mem - отправляет мем c спортсменами
 /emo - отправляет эмодзи
                 """)

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['par'])
def send_pass(message):
    bot.reply_to(message, gen_pass(10))

@bot.message_handler(commands=['cube'])
def send_cube(message):
    dice_result = bot.send_dice(message.chat.id, emoji='🎲')

@bot.message_handler(commands=['ball'])
def send_cube(message):
    dice_result = bot.send_dice(message.chat.id, emoji='⚽')

@bot.message_handler(commands=['mem'])
def send_mem(message):
    with open(random.choice(images), 'rb') as f:
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['emo'])
def send_emo(message):
    bot.reply_to(message, gen_emodji())

"""
@bot.message_handler(func=lambda message: True)
def respond(message):
    user_text = message.text
    answer = generate_answer(user_text)
    bot.reply_to(message, answer)
"""
bot.polling()
