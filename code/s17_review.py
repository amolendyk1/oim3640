import yfinance as yf

stock = yf.Ticker('AAPL')
info = stock.info            # a dict!
print(info['shortName'])     # 'Apple Inc.'
print(info['currentPrice'])  # 229.87

info = yf.Ticker('AAPL').info
# 'shortName', 'city', 'longBusinessSummary',
# 'sector', 'fullTimeEmployees', ...

tickers = ['AAPL', 'NVDA', 'MSFT']
prices = {}
for t in tickers:
    prices[t] = yf.Ticker(t).info['currentPrice']

tickers.append('GOOG')

tickers = ['AAPL', 'NVDA', 'MSFT']