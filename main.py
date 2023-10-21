from classes import Market, Product
from funcs import getstorelistcs, send_telegram
from cred import PATH

rawfile = [
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
]


marketjson = getstorelistcs(50667)

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
        categories = market.getoffercs()
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
                            price=offer["priceData"]["price"],
                            description=offer["subtitle"],
                        )
                    )
                else:
                    continue
    except IndexError:
        continue

with open(file=f"{PATH}liste.txt", mode="r") as rawfile:
    wantedlist = rawfile.readlines()

wantedlist = [i.strip() for i in wantedlist]

print(wantedlist)


for w in wantedlist:
    for p in productinstancelist:
        if w.lower() in p.name.lower():
            print(
                p.name,
                p.description,
                p.price,
                p.store.name,
                p.store.street,
                p.store.zipcode,
                p.store.city,
                # p.store.openuntil,
            )
            string_to_send = f"{p.name} \n{p.description} \n{p.price} \n{p.store.name} \n{p.store.street} \n{p.store.zipcode} {p.store.city}"

            send_telegram(string_to_send)
