from typing import List


def maxProfit(prices: List[int]) -> int:
    """t O(n) / s O(1)"""
    length, min_price, max_profit = len(prices) - 1, prices[0], 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


def max_profit(prices: List[int]) -> int:
    """t O(n) / s O(1)"""
    l, r, _max_profit = 0, 1, 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            _max_profit = max(profit, _max_profit)
        else:
            l = r
        r += 1
    return _max_profit


if __name__ == '__main__':
    print(max_profit([7, 1, 5, 3, 6, 4]))
