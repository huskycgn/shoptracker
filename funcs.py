from zenrows import ZenRowsClient
from cred import API_KEY, TELE_TOKEN, TELE_CHAT_ID
import telebot


def getstorelist(zipcode):
    urlstring = f"https://www.rewe.de/api/marketsearch?searchTerm={zipcode}"
    client = ZenRowsClient(API_KEY)

    response = client.get(urlstring)
    # print(response.json())
    return response.json()


def send_telegram(message):
    bot = telebot.TeleBot(token=TELE_TOKEN)
    bot.send_message(chat_id=TELE_CHAT_ID, text=message)
