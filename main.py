from classes import Market, Product
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
    "Red Bull",
    "Mozzarella",
]


marketjson = getstorelist(50667)

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


for market in marketinstancelist:
    try:
        categories = market.getofferszen()
        for cat in categories:
            # print(cat)
            offerlist = cat["offers"]
            # print(offerlist)
            for offer in offerlist:
                if offer["cellType"] == "DEFAULT" and offer["overline"] == "":
                    # print(offer)
                    productinstancelist.append(
                        Product(
                            store=market,
                            name=offer["title"],
                            price=offer["priceData"]["price"] or None,
                        )
                    )
                else:
                    continue
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
#             string_to_send = f"{p.name} {p.price} {p.store.name} {p.store.street} {p.store.zipcode} {p.store.city} {p.store.openuntil}"
# send_telegram(string_to_send)
