from classes import Market, Product
from requests import request
from funcs import getstorelist, send_telegram

wantedlist = [
    "Cheddar",
    "Felix",
    "Aperol",
    "Vodka",
    "Avocado",
    "Laktosefrei",
    "Coca-Cola",
    "Beinscheibe",
    "Kohle",
]

# marketjson = request(
#     method="GET", url="https://www.rewe.de/api/marketsearch?searchTerm=50667"
# )


marketjson = getstorelist(50667)

# print(marketjson.json())

marketdict = marketjson

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
            openuntil=m["openingInfo"],
        )
    )


marketofferdict = {}

for market in marketinstancelist:
    # pprint(market.marketid)
    marketofferdict[market.marketid] = {}
    try:
        marketoffers = market.getofferszen()
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
                p.store.openuntil,
            )
            string_to_send = f"{p.name} {p.price} {p.store.name} {p.store.street} {p.store.zipcode} {p.store.city} {p.store.openuntil}"
            send_telegram(string_to_send)
