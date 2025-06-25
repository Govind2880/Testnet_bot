from basic_bot import BasicBot

def main():
    print("Welcome to Binance Futures Testnet Bot")
    api_key = input("Enter the api key")
    api_secret = input("Enter the secret key")
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
