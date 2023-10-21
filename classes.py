import cloudscraper


class Market:
    def __init__(self, name, marketid, street, zipcode, city, openuntil):
        self.name = name
        self.openuntil = openuntil
        self.city = city
        self.zipcode = zipcode
        self.street = street
        self.marketid = marketid

    def getoffercs(self):
        scraper = cloudscraper.create_scraper(delay=10, browser="chrome")
        url = f"https://mobile-api.rewe.de/api/v3/all-offers?marketCode={self.marketid}"
        result = scraper.get(url).json()["categories"]
        return result


class Product:
    def __init__(self, name, price, store, description):
        self.store = store
        self.price = price
        self.name = name
        self.description = description
