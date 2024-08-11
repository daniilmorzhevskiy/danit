# bot.py
import telebot
import requests
import json

API_KEY = '6357348086:AAELOvtJrklUWEkUKI0gnAUrmMxD2iDaKY0'
MONOBANK_API_URL = 'https://api.monobank.ua/bank/currency'

bot = telebot.TeleBot(API_KEY)

# Завантаження курсу валют з Monobank API
def get_currency_rate():
    try:
        response = requests.get(MONOBANK_API_URL)
        response.raise_for_status()  # Перевірка на успішність запиту
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Помилка запиту до API Monobank: {e}")
        return []


def save_query(query):
    try:
        with open('storage.json', 'r') as file:
            queries = json.load(file)
    except FileNotFoundError:
        queries = []

    queries.append(query)
    
    with open('storage.json', 'w') as file:
        json.dump(queries, file)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Вітаю! Я бот для конвертації валют. Введіть суму та оберіть валюту для конвертації.")


@bot.message_handler(func=lambda message: True)
def handle_amount(message):
    try:
        amount = float(message.text)
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('USD', 'EUR', 'PLN')
        bot.send_message(message.chat.id, "Оберіть цільову валюту:", reply_markup=markup)
        bot.register_next_step_handler(message, lambda m: handle_conversion(m, amount))
    except ValueError:
        bot.reply_to(message, "Будь ласка, введіть коректну суму.")

# Конвертація валюти
def handle_conversion(message, amount):
    target_currency = message.text
    rates = get_currency_rate()

    if not rates:
        bot.send_message(message.chat.id, "Не вдалося отримати дані з API Monobank.")
        return

    currency_codes = {
        'USD': 840,
        'EUR': 978,
        'PLN': 985
    }
    
    if target_currency not in currency_codes:
        bot.send_message(message.chat.id, "Невідома валюта.")
        return
    
    target_currency_code = currency_codes[target_currency]
    uah_rate = next((item for item in rates if item["currencyCodeA"] == target_currency_code and item["currencyCodeB"] == 980), None)

    if uah_rate is None:
        bot.send_message(message.chat.id, f"Не вдалося знайти курс валюти для {target_currency} -> UAH.")
        return
    
    rate = uah_rate.get('rateSell')
    if rate is None:
        bot.send_message(message.chat.id, f"Не вдалося отримати курс продажу для {target_currency} -> UAH.")
        return
    
    result = amount / rate
    bot.send_message(message.chat.id, f"{amount} UAH = {result:.2f} {target_currency}")
    save_query({"amount": amount, "target_currency": target_currency, "result": result})

bot.polling()
