import math

NEG_INF = -10**18

def max_profit_dp (prices, k, fee):
    """
    Dynamic Programming trading optimizer.

    prices: list of daily prices
    k: max number of completed trades
    fee: transaction cost applied on sell
    """

    n = len(prices)
    if n == 0 or k == 0:
        return 0
    
    # cash[j]: max profit NOT holding with j completed trades
    # hold[j] max profit HOLDING with j completed trades

    cash = [0] * (k+1)
    hold = [NEG_INF] * (k+1)

    #Day 0 Initilization: buying is allowed
    for j in range(k+1):
        hold[j] = -prices[0]

    for t in range (1, n):
        price = prices[t]
        prev_cash = cash[:]
        prev_hold = hold[:]

        for j in range(k+1):
            # hold or buy
            hold[j] = max (prev_hold[j] # Keep holding
                           ,
                            prev_cash[j] - fee # Buy today
            ) 

            # sell (consume on trae)
            if j > 0:
                cash[j] = max(
                    prev_cash[j],  #Keep not holding
                    prev_hold[j-1] + price - fee # Sell today
                )
            else:
                cash[j] = prev_cash[j]
    return max(cash)