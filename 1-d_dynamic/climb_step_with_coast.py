from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    one, two, index = cost[0], cost[1], 2
    while index < len(cost):
        cur = min(one, two) + cost[index]
        one = two
        two = cur
        index += 1
    return min(one, two)


cost = [10, 15, 20, 5, 3]
print(minCostClimbingStairs(cost))
