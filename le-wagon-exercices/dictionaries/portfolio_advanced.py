# pylint: disable=missing-docstring

# TODO: start by defining a `portfolio` using a dict!

portfolio = {
  "AAPL": {
    "volume": 10,
    "strike": 154.12
  },
  "GOOG": {
    "volume": 2,
    "strike": 812.56
  },
  "TSLA": {
    "volume": 12,
    "strike": 342.12
  },
  "META": {
    "volume": 18,
    "strike": 209.0
  }
}

print(portfolio['TSLA']['volume'])
print(portfolio['GOOG']['strike'])

# Define the market prices
market = {
  "AAPL":  198.84,
  "GOOG": 1217.93,
  "TSLA":  267.66,
  "META":    179.06
}


# Calculate P&L for each stock and the overall portfolio
total_pl = 0

for stock_symbol, stock_data in portfolio.items():
    volume = stock_data["volume"]
    strike = stock_data["strike"]
    
    if stock_symbol in market:
        spot_price = market[stock_symbol]
        current_value = volume * spot_price
        initial_value = volume * strike
        pl = current_value - initial_value
        
        print(f"P&L for {stock_symbol}: {pl}")
        total_pl += pl
    else:
        print(f"No market data for {stock_symbol}")

print(f"Total P&L for the portfolio: {total_pl}")
