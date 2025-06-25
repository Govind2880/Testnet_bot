import logging
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException
import os

# Enable logging
logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)

        # Set base URL for Futures Testnet
        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        # Add a longer recvWindow (optional)
        self.client.REQUEST_PARAMS = {
            'recvWindow': 60000
        }

        # Sync local time with Binance server time
        self.client.futures_time()
        
    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == "buy" else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logging.info(f"Market Order: {order}")
            return order
        except BinanceAPIException as e:
            logging.error(f"Market Order Failed: {e}")
            return {"error": str(e)}

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == "buy" else SIDE_SELL,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price
            )
            logging.info(f"Limit Order: {order}")
            return order
        except BinanceAPIException as e:
            logging.error(f"Limit Order Failed: {e}")
            return {"error": str(e)}

    def place_stop_limit_order(self, symbol, side, quantity, price, stop_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == "buy" else SIDE_SELL,
                type=ORDER_TYPE_STOP,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price,
                stopPrice=stop_price
            )
            logging.info(f"Stop-Limit Order: {order}")
            return order
        except BinanceAPIException as e:
            logging.error(f"Stop-Limit Order Failed: {e}")
            return {"error": str(e)}
