import csv
from datetime import datetime

# Hardcoded stock prices (can be updated anytime)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 300
}

def get_user_input():
    portfolio = {}

    print("\n📊 Enter your stock portfolio (type 'done' to finish):")

    while True:
        stock = input("Enter stock symbol: ").upper()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print("❌ Stock not available. Try again.")
            continue

        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
            if quantity <= 0:
                print("❌ Quantity must be positive.")
                continue
        except ValueError:
            print("❌ Invalid input. Enter a number.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    return portfolio


def calculate_total(portfolio):
    total = 0
    details = []

    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        value = price * qty
        total += value
        details.append((stock, qty, price, value))

    return total, details


def display_portfolio(details, total):
    print("\n📈 Portfolio Summary:")
    print("-" * 40)

    for stock, qty, price, value in details:
        print(f"{stock} | Qty: {qty} | Price: ${price} | Value: ${value}")

    print("-" * 40)
    print(f"💰 Total Investment Value: ${total}")


def save_to_csv(details, total):
    filename = f"portfolio_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])

        for row in details:
            writer.writerow(row)

        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total])

    print(f"\n✅ Portfolio saved to {filename}")


def main():
    portfolio = get_user_input()

    if not portfolio:
        print("⚠️ No data entered.")
        return

    total, details = calculate_total(portfolio)
    display_portfolio(details, total)

    choice = input("\nDo you want to save this to a CSV file? (y/n): ").lower()
    if choice == 'y':
        save_to_csv(details, total)


if __name__ == "__main__":
    main()