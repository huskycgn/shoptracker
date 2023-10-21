import requests


class Market:
    def __init__(self, name, marketid, street, zipcode, city, openuntil):
        self.name = name
        self.openuntil = openuntil
        self.city = city
        self.zipcode = zipcode
        self.street = street
        self.marketid = marketid

    def getoffers(self):
        urlstring = (
            f"https://mobile-api.rewe.de/api/v3/all-offers?marketCode={self.marketid}"
        )
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,de-DE;q=0.7,de;q=0.6",
            "Cookie": "MRefererUrl=direct; _rdfa=s%3A293d731b-c2fd-4d5d-b8a0-14b3c065a5f6.iGTR%2By38sbwmoicD3Ec0MJsvIQfMUQCZUqzlO4tK3Sg; __cfruid=a46b145ddf6f72caa412dda02858fa1551a1c7d8-1697883881; _cfuvid=TAMfgqvzRxvtfoeORj_Mg6w71T9yYGMwSvMvcUYhvz8-1697883881226-0-604800000; rstp=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhZXMxOTIiOiI3ODljZGYyZDgyZTYwOTI1YmE3ZTFmZDM1MjEyNTZhMGM5ZTM1YjQxYmJkMzBkYzQ5OTcyODVmZTc5YzhiNzViZTYyYTlmMzk4NmQzZThiMGU0ODE3ZGNjMTQ4ZTE2YzA4NmI1N2E2YTQ1NDM0ODBjZjgzN2I5ZjJiYjFkZDY5YzRhYmRmNTBjNjg2YWU1ZjY2NGMxMmQzZmIwNjE2ZTI5N2JhYzdmNjEyOGNjOTRmMTg0MTRiYjhhZmU1NWE4ZjNjNTlmMjM3Mjk1MjJhMDA5NmIwNDU2MmNhNGM1MTY5ZmYyOWUxNWY1YTYxMzg0OGE5ZjE2ZGMyZWVmOTA2NzZkIiwiaWF0IjoxNjk3ODg0NjExLCJleHAiOjE2OTc4ODUyMTF9.KQpDQEWHF-eLbAwIJNYBJQkwYiMHsqf-YXcSSZNXn7KSjBrjATkCorQG1_jpBNwlENuAJ_mcToXgY_D1iX08Yw; AMCV_65BE20B35350E8DE0A490D45%40AdobeOrg=179643557%7CMCMID%7C77133610662574323669053874021339462149%7CMCAID%7CNONE%7CvVersion%7C5.5.0; icVarSave=; c_lpv_a=1697884633190|dir_direct_nn_nn_nn_nn_nn_nn_nn; cf_clearance=sNtZQlUbynvbjKForC.njOueMEeuSVt5Qj3dd0hsD10-1697884633-0-1-496c0783.6ff67196.8bc7fa69-0.2.1697884633; consentSettings={%22Usercentrics-Consent-Management-Platform%22:1%2C%22Adobe-Launch%22:1%2C%22Adobe-Experience-Cloud-Identity-Service%22:1%2C%22AWIN%22:1%2C%22reCAPTCHA%22:1%2C%22Cloudflare%22:1%2C%22Keycloak%22:1%2C%22gstatic-com%22:1%2C%22Google-Maps%22:1%2C%22JSDelivr%22:1%2C%22YouTube-Video%22:1%2C%22Google-AJAX%22:1%2C%22jQuery%22:1%2C%22Vimeo%22:1%2C%22Adobe-Analytics%22:1%2C%22Google-Ad-Manager-Basis%22:1%2C%22Funktionale-Cookies-und-Speicher%22:1%2C%22GfK-SENSIC%22:1%2C%22ChannelPilot%22:1%2C%22Adobe-Analytics-erweiterte-Web-Analyse%22:1%2C%22artegic-ELAINE-Software%22:1%2C%22Outbrain%22:1%2C%22RDFA-Technologie-Statistik-%22:1%2C%22Mouseflow%22:1%2C%22Facebook-Pixel%22:1%2C%22Microsoft-Advertising-Remarketing%22:1%2C%22Adform%22:1%2C%22Google-Ads-Conversion-Tracking%22:1%2C%22Google-Ads-Remarketing%22:1%2C%22Snapchat-Advertising%22:1%2C%22Pinterest-Tags%22:1%2C%22trbo%22:1%2C%22TikTok-Advertising%22:1%2C%22LinkedIn-Ads%22:1%2C%22Taboola%22:1%2C%22TradeDesk%22:1%2C%22DoubleClick-Floodlight%22:1%2C%22Cmmercl-ly%22:1%2C%22Google-Ad-Manager%22:1%2C%22RDFA-Technologie-Marketing-%22:1%2C%22tms%22:1%2C%22necessaryCookies%22:1%2C%22cmpPlatform%22:1%2C%22marketingBilling%22:1%2C%22fraudProtection%22:1%2C%22basicAnalytics%22:1%2C%22marketingOnsite%22:1%2C%22extendedAnalytics%22:1%2C%22serviceMonitoring%22:1%2C%22abTesting%22:1%2C%22conversionOptimization%22:1%2C%22feederAnalytics%22:1%2C%22personalAdsOnsite%22:1%2C%22remarketingOffsite%22:1%2C%22userProfiling%22:1%2C%22sessionMonitoring%22:1%2C%22targetGroup%22:1%2C%22advertisingOnsite%22:1}; __cf_bm=MCavGZo.iKI8k0VqXeoP19dLnKYVZghAFIZ0KdxHd78-1697892559-0-AVONHSd0ZhPeiO4S6AldTxzpoTBcsfm2bRgdndIuc1LYRRYPJ9uadmPq9hpPU2Y1aQKfAUJhTfhWJDREZd8cioY=",
        }
        rawlist = requests.get(url=urlstring, headers=headers)
        return rawlist.json()["categories"][0]["offers"]
