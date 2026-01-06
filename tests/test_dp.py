from strategies.dp import max_profit_dp

def test_simple_increasing():
    prices = [1, 2, 3, 4]
    assert max_profit_dp(prices, k=1) == 3

def test_simple_decreasing():
    prices = [4, 3, 2, 1]
    assert max_profit_dp(prices, k=2) == 0

def test_multiple_trades():
    prices = [3, 2, 6, 5, 0, 3]
    assert max_profit_dp(prices, k=2) == 7
    # buy at 2 sell at 6 (4)
    # buy at 0 sell at 3 (3)

def test_transaction_fee():
    prices = [1, 3, 2, 8, 4, 9]
    assert max_profit_dp(prices, k=2, fee=2) == 8

def test_single_day():
    prices = [5]
    assert max_profit_dp(prices, k=3) == 0

print("All DP tests passed.")
