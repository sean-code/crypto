# This code assumes that you have access to up-to-date market data for USDT futures across the different exchanges

# Define the different exchanges and their respective prices for USDT futures
kucoin_price = 100
binance_price = 101
huobi_price = 102
okx_price = 99
coinbase_price = 98
bybit_price = 97
bitget_price = 96
bitfinex_price = 95

# Calculate the highest and lowest prices among the exchanges
highest_price = [kucoin_price, binance_price, huobi_price, okx_price, coinbase_price, bybit_price, bitget_price, bitfinex_price].max
lowest_price = [kucoin_price, binance_price, huobi_price, okx_price, coinbase_price, bybit_price, bitget_price, bitfinex_price].min

# Calculate the potential profit from buying at the lowest price and selling at the highest price
potential_profit = (highest_price - lowest_price) / lowest_price

# Check if the potential profit is greater than 0.1%
if potential_profit > 0.001
  puts "Arbitrage opportunity found! Potential profit: #{(potential_profit * 100)}%"
else
  puts "No arbitrage opportunity found."
end
