import ccxt;

exchanges = ['kucoin', 'binance', 'huobi', 'okex', 'coinbase', 'bybit', 'bitget', 'bitfinex']
symbols = ['BTC/USDT', 'ETH/USDT', 'ADA/USDT', 'DOT/USDT', 'UNI/USDT', 'SOL/USDT', 'XRP/USDT', 'LTC/USDT']

exchange_objects = [getattr(ccxt, exchange)() for exchange in exchanges]
for exchange_object in exchange_objects:
    exchange_object.load_markets()

for i in range(len(symbols)):
    symbol = symbols[i]
    prices = []
    for exchange_object in exchange_objects:
        if symbol in exchange_object.symbols and 'future' in exchange_object.symbols[symbol]:
            orderbook = exchange_object.fetch_order_book(symbol)
            bid = orderbook['bids'][0][0] if len(orderbook['bids']) > 0 else None
            ask = orderbook['asks'][0][0] if len(orderbook['asks']) > 0 else None
            if bid and ask:
                prices.append(ask)
    if len(prices) >= 2:
        min_price = min(prices)
        max_price = max(prices)
        spread = max_price - min_price
        spread_percentage = spread / min_price * 100
        if spread_percentage > 0.1:
            print(f"Arbitrage opportunity found for {symbol}: {spread_percentage:.2f}% between {exchanges[prices.index(min_price)]} and {exchanges[prices.index(max_price)]}")
