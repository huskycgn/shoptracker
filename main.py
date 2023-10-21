from classes import Market, Product
from requests import request
from pprint import pprint

wantedlist = ["Cheddar", "Felix"]

marketjson = request(
    method="GET", url="https://www.rewe.de/api/marketsearch?searchTerm=50667"
)

# print(marketjson.json())

marketdict = marketjson.json()

marketinstancelist = []
productinstancelist = []

for m in marketdict:
    # print(m)
    marketinstancelist.append(
        Market(
            name=m["companyName"],
            marketid=m["wwIdent"],
            street=m["contactStreet"],
            zipcode=m["contactZipCode"],
            city=m["contactCity"],
            openuntil=m["openingInfo"]["isOpen"]["until"],
        )
    )


marketofferdict = {}

for market in marketinstancelist:
    # pprint(market.marketid)
    marketofferdict[market.marketid] = {}
    try:
        marketoffers = market.getoffers()
        for mo in marketoffers:
            # print(mo["title"])
            marketofferdict[market.marketid][mo["title"]] = mo["priceData"]["price"]
            productinstancelist.append(
                Product(
                    store=market,
                    name=mo["title"],
                    price=mo["priceData"]["price"],
                )
            )
    except IndexError:
        continue


for w in wantedlist:
    for p in productinstancelist:
        if w.lower() in p.name.lower():
            print(
                p.name,
                p.price,
                p.store.name,
                p.store.street,
                p.store.zipcode,
                p.store.city,
            )
