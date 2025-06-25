from basic_bot import BasicBot

def main():
    print("Welcome to Binance Futures Testnet Bot")
    api_key = "2192e7b6d520b0e986f935369cea2755e2403ed2bb2d4d7f53a28f6ad4e0bd06"
    api_secret = "f2b6fc92ae51021df49c6629602c9704c787c5cf96c658df62b7a0119a255868"
    bot = BasicBot(api_key, api_secret)

    while True:
        print("\nAvailable Order Types:\n1. Market\n2. Limit\n3. Stop-Limit\n4. Exit")
        choice = input("Select option (1-4): ")

        if choice == '4':
            break

        symbol = input("Enter trading pair (e.g., BTCUSDT): ").upper()
        side = input("Buy or Sell?: ").lower()
        quantity = float(input("Quantity: "))

        if choice == '1':
            result = bot.place_market_order(symbol, side, quantity)

        elif choice == '2':
            price = float(input("Limit Price: "))
            result = bot.place_limit_order(symbol, side, quantity, price)

        elif choice == '3':
            stop_price = float(input("Stop Price: "))
            price = float(input("Limit Price: "))
            result = bot.place_stop_limit_order(symbol, side, quantity, price, stop_price)

        else:
            print("Invalid choice.")
            continue

        print("Order Result:", result)

if __name__ == "__main__":
    main()
