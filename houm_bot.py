import telebot
import random
from bot_logic import gen_pass, gen_emodji, flip_cube, get_duck_image_url, get_fox_image_url, get_dog_image_url
import os
import asyncio


bot = telebot.TeleBot("7557234987:AAEPYBFDmfncr2gEVD4oWF1oTC0Yn0Ymk8A")  # Не забудьте заменить на ваш токен

images = [r'C:\Users\User\Python\t_bot\images\mem.jpeg',
          r'C:\Users\User\Python\t_bot\images\mem2.jpeg',
          r'C:\Users\User\Python\t_bot\images\mem3.jpeg']


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['help'])
def send_hello(message):
    bot.reply_to(message, """
                 /start - запуск бота
                 /bye - прощание с ботом
                 /par - генерация рандомного пароля
                 /cube - бросок кубика
                 /ball - пнуть мяч
                 /mem - отправляет мем
                 /emo - отправляет эмодзи
                 /duck - отправляет картинку с уткой
                 отправь сообщение и нейросеть ответит на него""")

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

@bot.message_handler(commands=['duck'])
async def send_duck(message):
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

@bot.message_handler(commands=['fox'])
async def send_duck(message):
    image_url = get_fox_image_url()
    bot.reply_to(message, image_url)

@bot.message_handler(commands=['dog'])
async def send_duck(message):
    image_url = get_dog_image_url()
    bot.reply_to(message, image_url)
    


bot.polling()
