from zenrows import ZenRowsClient
from cred import API_KEY


class Market:
    def __init__(self, name, marketid, street, zipcode, city, openuntil):
        self.name = name
        self.openuntil = openuntil
        self.city = city
        self.zipcode = zipcode
        self.street = street
        self.marketid = marketid

    def getofferszen(self):
        urlstring = (
            f"https://mobile-api.rewe.de/api/v3/all-offers?marketCode={self.marketid}"
        )
        client = ZenRowsClient(API_KEY)

        response = client.get(urlstring)
        return response.json()["categories"]


class Product:
    def __init__(self, name, price, store):
        self.store = store
        self.price = price
        self.name = name
