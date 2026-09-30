# TASK 2: Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        price = stock_prices[stock]
        investment = price * quantity

        print(f"{stock} Price: ${price}")
        print(f"Investment: ${investment}")

        total_investment += investment

    except ValueError:
        print("Please enter a valid quantity.")

print("\n===== PORTFOLIO SUMMARY =====")
print(f"Total Investment: ${total_investment}")

# Save result to a text file
with open("portfolio_result.txt", "w") as file:
    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("=======================\n")
    file.write(f"Total Investment: ${total_investment}\n")

print("Result saved to portfolio_result.txt")
