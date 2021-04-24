from binance.client import Client
import json
import threading
import time

CONFIG_API_KEY_KEY = "apiKey"
CONFIG_API_SECRET_KEY = "apiSecret"
CONFIG_MILLISECONDS_BETWEEN_PRICE_QUERIES_KEY = "millisecondsBetweenPriceQueries"

ms_between_price_queries = 0
did_buy = False


def main():
    with open('config.json', 'r') as config:
        config = json.loads(config.read())

    client = Client(config[CONFIG_API_KEY_KEY], config[CONFIG_API_SECRET_KEY])

    global ms_between_price_queries
    ms_between_price_queries = config[CONFIG_MILLISECONDS_BETWEEN_PRICE_QUERIES_KEY]

    #print(client.get_symbol_ticker(symbol="BNBEUR"))

    while True:
        a = input()


def run_bot(client, symbol):
    last_price = client.get_symbol_ticker(symbol=symbol)
    pre_buy_ref_price = 0
    pre_sell_ref_price = 0
    while True:
        price = client.get_symbol_ticker(symbol=symbol)
        ref_price = pre_buy_ref_price if not did_buy else pre_sell_ref_price
        percent_change = (price - (pre_sell_ref_price if did_buy else pre_buy_ref_price)) / price

        if not did_buy:
            ref_price = pre_buy_ref_price
            percent_change = (price - pre_buy_ref_price) / price







main()
