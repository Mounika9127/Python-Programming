# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3400,
    "MSFT": 300
}

portfolio = {}

# Input section
while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock in stock_prices:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    else:
        print("Stock not found in the predefined list. Try again.")

# Calculate total investment
total_value = 0
print("\n--- Portfolio Summary ---")
for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_value += value
    print(f"{stock}: {quantity} shares x ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment Value: ${total_value}")

# Optional: Save to a file
save = input("Would you like to save the result to a file? (yes/no): ").lower()
if save == 'yes':
    with open("portfolio_summary.txt", "w") as file:
        file.write("--- Portfolio Summary ---\n")
        for stock, quantity in portfolio.items():
            value = stock_prices[stock] * quantity
            file.write(f"{stock}: {quantity} shares x ${stock_prices[stock]} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}")
    print("Portfolio saved to 'portfolio_summary.txt'")
