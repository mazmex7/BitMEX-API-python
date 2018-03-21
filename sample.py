#!/usr/bin/env python

from bitmex import bitmex

api_key = '' # your api key
api_secret = '' # your api secret

bitmex_cli = bitmex(test=False, api_key=api_key, api_secret=api_secret)

### public api test

### get orderbook
# orderbook = bitmex_cli.OrderBook.OrderBook_getL2(symbol='XBTUSD', depth=20).result()
# print( orderbook )


### private api test ( needs api key and secret )

### get your orders
# orders = bitmex_cli.Order.Order_getOrders(symbol='XBTUSD', reverse=True).result()
# print( orders )
