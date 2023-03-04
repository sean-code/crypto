const ccxt = require('ccxt');

const exchanges = ['kucoin', 'binance', 'huobipro', 'okex', 'coinbasepro', 'bybit', 'bitget', 'bitfinex'];
const markets = [];

(async () => {
  for (let exchange of exchanges) {
    const exchangeObj = new ccxt[exchange]();
    const exchangeMarkets = await exchangeObj.loadMarkets();
    for (let market of Object.keys(exchangeMarkets)) {
      if (market.includes('USDT') && market.includes('Futures')) {
        markets.push({ exchange, market });
      }
    }
  }

  const opportunities = [];

  for (let i = 0; i < markets.length; i++) {
    const { exchange: exchange1, market: symbol1 } = markets[i];
    for (let j = i + 1; j < markets.length; j++) {
      const { exchange: exchange2, market: symbol2 } = markets[j];
      if (exchange1 !== exchange2 && symbol1 === symbol2) {
        const exchange1Obj = new ccxt[exchange1]();
        const exchange2Obj = new ccxt[exchange2]();
        const orderbook1 = await exchange1Obj.fetchOrderBook(symbol1);
        const orderbook2 = await exchange2Obj.fetchOrderBook(symbol2);
        const bestBid1 = orderbook1.bids[0][0];
        const bestAsk2 = orderbook2.asks[0][0];
        const rate1To2 = bestBid1 / bestAsk2;
        const rate2To1 = bestAsk2 / bestBid1;
        if (rate1To2 > 1.001) {
          opportunities.push({ exchange1, symbol1, exchange2, symbol2, rate: rate1To2 });
        }
        if (rate2To1 > 1.001) {
          opportunities.push({ exchange1: exchange2, symbol1: symbol2, exchange2: exchange1, symbol2: symbol1, rate: rate2To1 });
        }
      }
    }
  }

  console.log(opportunities);
})();






// Solution 2
// This code assumes that you have access to up-to-date market data for USDT futures across the different exchanges

// Define the different exchanges and their respective prices for USDT futures
const kucoinPrice = 100;
const binancePrice = 101;
const huobiPrice = 102;
const okxPrice = 99;
const coinbasePrice = 98;
const bybitPrice = 97;
const bitgetPrice = 96;
const bitfinexPrice = 95;

// Calculate the highest and lowest prices among the exchanges
const highestPrice = Math.max(kucoinPrice, binancePrice, huobiPrice, okxPrice, coinbasePrice, bybitPrice, bitgetPrice, bitfinexPrice);
const lowestPrice = Math.min(kucoinPrice, binancePrice, huobiPrice, okxPrice, coinbasePrice, bybitPrice, bitgetPrice, bitfinexPrice);

// Calculate the potential profit from buying at the lowest price and selling at the highest price
const potentialProfit = (highestPrice - lowestPrice) / lowestPrice;

// Check if the potential profit is greater than 0.1%
if (potentialProfit > 0.001) {
  console.log("Arbitrage opportunity found! Potential profit: " + (potentialProfit * 100) + "%");
} else {
  console.log("No arbitrage opportunity found.");
}





//Solution 3 -fixed
// Define the different exchanges and their respective prices for USDT futures
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

// Determine the exchange with the lowest price
let lowestExchange, lowestPrice = Number.MAX_VALUE;
for (let exchange in prices) {
  if (prices[exchange] < lowestPrice) {
    lowestExchange = exchange;
    lowestPrice = prices[exchange];
  }
}

// Determine the exchange with the highest price relative to the lowest price
let highestExchange, highestPrice = Number.MIN_VALUE;
for (let exchange in prices) {
  let price = prices[exchange];
  if (price > highestPrice && price > lowestPrice) {
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
