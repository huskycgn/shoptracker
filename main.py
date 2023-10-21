from classes import Market
from requests import request
from pprint import pprint

wantedlist = ["Cheddar", "Felix"]

marketjson = request(
    method="GET", url="https://www.rewe.de/api/marketsearch?searchTerm=50667"
)

# print(marketjson.json())

marketdict = marketjson.json()

marketinstancelist = []

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

# m1 = Market(
#     name=marketdict[0]['companyName'],
#     marketid=marketdict[0]['wwIdent'],
#     street=marketdict[0]['contactStreet'],
#     zipcode=marketdict[0]['contactZipCode'],
#     city=marketdict[0]['contactCity'],
#     openuntil=marketdict[0]['openingInfo']['isOpen']['until'],)

# print(m1.__dict__)

marketofferdict = {}

for market in marketinstancelist:
    # pprint(market.marketid)
    marketofferdict[market.marketid] = {}
    try:
        marketoffers = market.getoffers()
        for mo in marketoffers:
            # print(mo["title"])
            marketofferdict[market.marketid][mo["title"]] = mo["priceData"]["price"]
    except IndexError:
        pprint("No offers")

# print(marketofferdict)

# for o in marketofferdict:
#     proddict = marketofferdict[o]
#     if "Felix Katzennahrung" in proddict:
#         print(proddict["Felix Katzennahrung"])
#     else:
#         print(False)

for o in marketofferdict:
    proddict = marketofferdict[o]
    substring = "Felix"
    result = {}
    for keys, values in marketofferdict[o].items():
        if substring in keys:
            result[keys] = keys
    print(result)
