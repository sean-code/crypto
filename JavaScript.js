


// Final Solution
const prices = {
  "kucoin": 100,
  "binance": 101,
  "huobi": 102,
  "okx": 99,
  "coinbase": 98,
  "bybit": 97,
  "bitget": 96,
  "bitfinex": 95
};

// Determine the exchange with the lowest price and the exchange with the highest price relative to the lowest price
let lowestExchange, lowestPrice, highestExchange, highestPrice;
for (const [exchange, price] of Object.entries(prices)) {
  if (lowestPrice === undefined || price < lowestPrice) {
    lowestExchange = exchange;
    lowestPrice = price;
  }
  if (highestPrice === undefined || price / lowestPrice > highestPrice / lowestPrice) {
    highestExchange = exchange;
    highestPrice = price;
  }
}

// Calculate the potential profit from buying at the lowest price and selling at the highest price
const potentialProfit = (highestPrice - lowestPrice) / lowestPrice;

// Check if the potential profit is greater than 0.1%
if (potentialProfit > 0.001) {
  console.log(`Arbitrage opportunity found! Buy at ${lowestExchange} for ${lowestPrice} and sell at ${highestExchange} for ${highestPrice}. Potential profit: ${(potentialProfit * 100)}%`);
} else {
  console.log("No arbitrage opportunity found.");
}
