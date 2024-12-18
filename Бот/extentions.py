import requests
import json


class ConvertionError(Exception):
    pass


keys = {
    'биткоин': 'BTC',
    'доллар': 'USD',
    'эфириум': 'ETH'
}


class CryptoConverter():
    @staticmethod
    def convertion(fsym, tsyms, amount):
        api = f'https://min-api.cryptocompare.com/data/price?fsym={keys[fsym]}&tsyms={keys[tsyms]}'
        r = requests.get(api)
        text = json.loads(r.content)[keys[tsyms]]
        text = float(text)*float(amount)
        return text
