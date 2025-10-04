import telebot
from g4f.client import Client

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("7557234987:AAEPYBFDmfncr2gEVD4oWF1oTC0Yn0Ymk8A")

prompt = []
history = []
def send_request_gpt(content: str):
  global history, prompt, response_text

  
  history.append({'role': 'system', 'content': 'ты - олег и всё'},{"role": "user", "content": message.chat.id})

  client = Client()
  response = client.chat.completions.create(
  model="GPT-4",
  messages=messages, # указываем полный запрос с ролью GPT
  web_search=False)

  response_text = response.choices[0].message.content 

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye ")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "/start - запуск бота,\n /hello -  приветсвие,\n/help - help,\n/bye - прощание")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    # Отправляем обратно сообщение, которое прислал пользователь
    bot.send_message(message.chat.id, f"Ты сказал: '{message.text}' - Мой ответ: {response_text}")



# Запускаем бота
bot.polling()
