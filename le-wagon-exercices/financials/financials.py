# pylint: disable=missing-docstring

# TODO: 1st exercise: Define the `forward_price` function

# TODO: 2nd exercise: Define the `short_pnl` function

import math

def forward_price(spot, interest_rate, time):
    
    forward_price_unrounded= spot * math.exp(interest_rate*time)
    forward_price= round(forward_price_unrounded, 2)
    return forward_price

spot=100
interest_rate=0.05
time=1

calculated_forward_price= forward_price(spot, interest_rate, time)

print(f"The forward price is: {calculated_forward_price}")


def short_pnl(positions, mtm):
    
    short_pnl=0
    for strike, market_value in zip(positions, mtm):
        individual_pnl= strike - market_value
        short_pnl +=individual_pnl
        
    return short_pnl

positions= [100, 140, 200]
mtm= [110, 120, 180]

short_pnl_result= short_pnl(positions, mtm)
print(f"The P&L is: {short_pnl_result}")



