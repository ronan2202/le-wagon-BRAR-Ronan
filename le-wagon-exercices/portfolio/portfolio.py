# pylint: disable=missing-docstring

aapl = [ 10, 154.12 ]
goog = [  2, 812.56 ]
tsla = [ 12, 342.12 ]
fb   = [ 18, 209.0  ]

portfolio = [ aapl, goog, tsla, fb ]
print (portfolio)

fb_stocks_counts= portfolio[3][0]
print(fb_stocks_counts)


market = [ 198.84, 1217.93, 267.66, 179.06 ]

aaplpnl= portfolio[0][0]*portfolio[0][1] - (portfolio[0][0]*market[0])
googpnl= portfolio[1][0]*portfolio[1][1] - (portfolio[1][0]*market[1])
tslapnl= portfolio[2][0]*portfolio[2][1] - (portfolio[2][0]*market[2])
fbpnl= portfolio[3][0]*portfolio[3][1] - (portfolio[3][0]*market[3])

pnl= [aaplpnl, googpnl, tslapnl, fbpnl]

print(pnl)
