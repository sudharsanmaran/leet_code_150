from typing import Deque, List
import heapq


def maxProfit_heap(prices: List[int]) -> int:
    """t O(n * (n + n)) / s O(n)"""
    max_profit = 0
    # O(n)
    for idx, price in enumerate(prices):
        # O(n)
        max_heap = [price * -1 for price in prices[idx + 1 :]]
        # O(n)
        heapq.heapify(max_heap)
        if max_heap and price < max_heap[0] * -1:
            max_profit = max(max_profit, (max_heap[0] * -1) - price)
    return max_profit


def maxProfit_nested_loop(prices: List[int]) -> int:
    """t O(n^2) / s O(1)"""
    max_profit, n = 0, len(prices)
    for i in range(n):
        for j in range(i + 1, n):
            max_profit = max(max_profit, prices[j] - prices[i])
    return max_profit


def maxProfit_sort(prices: List[int]) -> int:
    """t O(n^2) / s O(n)"""
    max_profit = 0
    # O(n * log n)
    sorted_prices = sorted(prices)
    # O(n)
    for price in prices:
        if price < sorted_prices[-1]:
            max_profit = max(max_profit, (sorted_prices[-1]) - price)
        # O(n)
        sorted_prices.remove(price)
    return max_profit


def maxProfit_aux_list(prices):
    """t O(n + n) / s O(n)"""
    # used deque
    # max_sell_amount = Deque()
    # max_sell_amount.append(0)
    # for i in range(len(prices) - 1, 0, -1):
    #     if prices[i] > max_sell_amount[0]:
    #         max_sell_amount.appendleft(prices[i])
    #     else:
    #         max_sell_amount.appendleft(max_sell_amount[0])

    # used list
    n = len(prices)
    max_sell_amount = [0] * (n + 1)
    for i in range(n - 1, 0, -1):
        max_sell_amount[i] = max(prices[i], max_sell_amount[i + 1])
    max_profit = 0
    for idx, price in enumerate(prices):
        max_profit = max(max_profit, (max_sell_amount[idx + 1] - price))
    return max_profit


def maxProfit_1(prices: List[int]) -> int:
    """ t O(n) / s O(1)"""
    max_profit, min_price = 0, prices[0]
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit


if __name__ == "__main__":
    assert maxProfit_aux_list([7, 1, 5, 3, 6, 4]) == 5
