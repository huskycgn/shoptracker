from cred import TELE_TOKEN, TELE_CHAT_ID
import telebot
import cloudscraper


def getstorelistcs(zipcode):
    url = f"https://www.rewe.de/api/marketsearch?searchTerm={zipcode}"
    scraper = cloudscraper.create_scraper(delay=10, browser="chrome")
    result = scraper.get(url).json()
    return result


def send_telegram(message):
    bot = telebot.TeleBot(token=TELE_TOKEN)
    bot.send_message(chat_id=TELE_CHAT_ID, text=message)
