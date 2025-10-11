import random
import os
import requests

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)

def get_duck_image_url():    
        url = 'https://random-d.uk/api/random'
        res = requests.get(url)
        data = res.json()
        return data['url']

def flip_cube():
    # Отсылаем кубик (игральный d6)
    dice_result = bot.send_dice(message.chat.id, emoji='🎲')
    
    # Если хотите вывести значение кубика после броска
    bot.reply_to(dice_result, f"Кубик выпал на {dice_result.dice.value}")
