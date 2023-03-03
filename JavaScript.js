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
