def test_greedy_simple_uptrend():
    prices = [1, 2, 3, 4]
    assert greedy_profit(prices, k=10) == 3


def test_greedy_simple_downtrend():
    prices = [4, 3, 2, 1]
    assert greedy_profit(prices, k=10) == 0
