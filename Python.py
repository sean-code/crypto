# import ccxt

# exchanges = [
#     'kucoin',
#     'binance',
#     'huobi',
#     'okex',
#     'coinbase',
#     'bybit',
#     'bitget',
#     'bitfinex'
# ]

# # instantiate exchange objects
# exchange_objs = {}
# for exchange_name in exchanges:
#     exchange_class = getattr(ccxt, exchange_name)
#     exchange_objs[exchange_name] = exchange_class()

# # fetch USDT futures prices
# usdt_futures_prices = {}
# for exchange_name, exchange_obj in exchange_objs.items():
#     try:
#         markets = exchange_obj.load_markets()
#         for symbol, market in markets.items():
#             if 'USDT' in symbol and 'futures' in market['type']:
#                 ticker = exchange_obj.fetch_ticker(symbol)
#                 usdt_futures_prices[f"{exchange_name}-{symbol}"] = ticker['last']
#     except ccxt.BaseError as e:
#         print(f"Failed to fetch prices from {exchange_name}: {e}")

# # find arbitrage opportunities
# arbitrage_opportunities = []
# for i, (exchange_symbol1, price1) in enumerate(usdt_futures_prices.items()):
#     exchange1, symbol1 = exchange_symbol1.split('-')
#     for exchange_symbol2, price2 in list(usdt_futures_prices.items())[i+1:]:
#         exchange2, symbol2 = exchange_symbol2.split('-')
#         if symbol1 == symbol2:
#             price_diff = abs(price1 - price2) / price1
#             if price_diff > 0.001:
#                 arbitrage_opportunities.append((exchange_symbol1, exchange_symbol2, price_diff))

# # print arbitrage opportunities
# if arbitrage_opportunities:
#     print("Arbitrage opportunities found:")
#     for opp in arbitrage_opportunities:
#         print(f"{opp[0]}: {usdt_futures_prices[opp[0]]} vs {opp[1]}: {usdt_futures_prices[opp[1]]}, price diff: {opp[2]*100:.2f}%")
# else:
#     print("No arbitrage opportunities found.")


# # => This code fetches USDT futures prices from the specified exchanges using the ccxt library, and then checks for price differences greater than 0.1% between pairs of exchanges for the same futures contract. If any arbitrage opportunities are found, the code prints out the exchange names, prices, and percentage differences.



# # Solution received

# #  => output of this code might look like based on historical data.
# # Let's say we ran this code with historical USDT futures prices from February 28, 2022. Here is an example output we might get:



# # Arbitrage opportunities found:
# # bybit-BTC/USDT-0325: 48794.5 vs bitfinex-BTCF0: 49543.0, price diff: 1.52%
# # bybit-BTC/USDT-0325: 48794.5 vs bitget-BTCUSDT0625: 49268.0, price diff: 0.97%
# # bybit-BTC/USDT-0325: 48794.5 vs coinbase-BTC-USD-0325: 49442.0, price diff: 1.33%
# # bybit-BTC/USDT-0325: 48794.5 vs huobi-BTC-USD-0325: 49561.6, price diff: 1.61%
# # bybit-BTC/USDT-0325: 48794.5 vs okex-BTC-USD-0325: 49334.0, price diff: 1.09%
# # bitfinex-BTCF0: 49543.0 vs bitget-BTCUSDT0625: 49268.0, price diff: 0.56%
# # bitfinex-BTCF0: 49543.0 vs coinbase-BTC-USD-0325: 49442.0, price diff: 0.20%
# # bitfinex-BTCF0: 49543.0 vs huobi-BTC-USD-0325: 49561.6, price diff: 0.04%
# # bitfinex-BTCF0: 49543.0 vs okex-BTC-USD-0325: 49334.0, price diff: 0.42%
# # bitget-BTCUSDT0625: 49268.0 vs coinbase-BTC-USD-0325: 49442.0, price diff: 0.35%
# # bitget-BTCUSDT0625: 49268.0 vs huobi-BTC-USD-0325: 49561.6, price diff: 0.59%
# # bitget-BTCUSDT0625: 49268.0 vs okex-BTC-USD-0325: 49334.0, price diff: 0.13%
# # coinbase-BTC-USD-0325: 49442.0 vs huobi-BTC-USD-0325: 49561.6, price diff: 0.24%
# # coinbase-BTC-USD-0325: 49442.0 vs okex-BTC-USD-0325: 49334.0, price diff: 0.22%
# # huobi-BTC-USD-0325: 49561.6 vs okex-BTC-USD-0325: 49334.0, price diff: 0.46%









# kucoin_price = 100
# binance_price = 101
# huobi_price = 102
# okx_price = 99
# coinbase_price = 98
# bybit_price = 97
# bitget_price = 96
# bitfinex_price = 95

# highest_price = max(kucoin_price, binance_price, huobi_price, okx_price, coinbase_price, bybit_price, bitget_price, bitfinex_price)
# lowest_price = min(kucoin_price, binance_price, huobi_price, okx_price, coinbase_price, bybit_price, bitget_price, bitfinex_price)

# potential_profit = (highest_price - lowest_price) / lowest_price

# if potential_profit > 0.001:
#     print(f"Arbitrage opportunity found! Potential profit: {(potential_profit * 100)}%")
# else:
#     print("No arbitrage opportunity found.")











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
