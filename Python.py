

# Final Solution
prices = {
    "kucoin": 100,
    "binance": 101,
    "huobi": 102,
    "okx": 99,
    "coinbase": 98,
    "bybit": 97,
    "bitget": 96,
    "bitfinex": 95
}

# Determine the exchange with the lowest price and the exchange with the highest price relative to the lowest price
lowest_exchange, lowest_price, highest_exchange, highest_price = None, None, None, None
for exchange, price in prices.items():
    if lowest_price is None or price < lowest_price:
        lowest_exchange, lowest_price = exchange, price
    if highest_price is None or price / lowest_price > highest_price / lowest_price:
        highest_exchange, highest_price = exchange, price

# Calculate the potential profit from buying at the lowest price and selling at the highest price
potential_profit = (highest_price - lowest_price) / lowest_price

# Check if the potential profit is greater than 0.1%
if potential_profit > 0.001:
    print(f"Arbitrage opportunity found! Buy at {lowest_exchange} for {lowest_price} and sell at {highest_exchange} for {highest_price}. Potential profit: {potential_profit * 100}%")
else:
    print("No arbitrage opportunity found.")
