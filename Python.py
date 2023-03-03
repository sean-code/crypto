import ccxt

exchanges = [
    'kucoin',
    'binance',
    'huobi',
    'okex',
    'coinbase',
    'bybit',
    'bitget',
    'bitfinex'
]

# instantiate exchange objects
exchange_objs = {}
for exchange_name in exchanges:
    exchange_class = getattr(ccxt, exchange_name)
    exchange_objs[exchange_name] = exchange_class()

# fetch USDT futures prices
usdt_futures_prices = {}
for exchange_name, exchange_obj in exchange_objs.items():
    try:
        markets = exchange_obj.load_markets()
        for symbol, market in markets.items():
            if 'USDT' in symbol and 'futures' in market['type']:
                ticker = exchange_obj.fetch_ticker(symbol)
                usdt_futures_prices[f"{exchange_name}-{symbol}"] = ticker['last']
    except ccxt.BaseError as e:
        print(f"Failed to fetch prices from {exchange_name}: {e}")

# find arbitrage opportunities
arbitrage_opportunities = []
for i, (exchange_symbol1, price1) in enumerate(usdt_futures_prices.items()):
    exchange1, symbol1 = exchange_symbol1.split('-')
    for exchange_symbol2, price2 in list(usdt_futures_prices.items())[i+1:]:
        exchange2, symbol2 = exchange_symbol2.split('-')
        if symbol1 == symbol2:
            price_diff = abs(price1 - price2) / price1
            if price_diff > 0.001:
                arbitrage_opportunities.append((exchange_symbol1, exchange_symbol2, price_diff))

# print arbitrage opportunities
if arbitrage_opportunities:
    print("Arbitrage opportunities found:")
    for opp in arbitrage_opportunities:
        print(f"{opp[0]}: {usdt_futures_prices[opp[0]]} vs {opp[1]}: {usdt_futures_prices[opp[1]]}, price diff: {opp[2]*100:.2f}%")
else:
    print("No arbitrage opportunities found.")


# => This code fetches USDT futures prices from the specified exchanges using the ccxt library, and then checks for price differences greater than 0.1% between pairs of exchanges for the same futures contract. If any arbitrage opportunities are found, the code prints out the exchange names, prices, and percentage differences.



