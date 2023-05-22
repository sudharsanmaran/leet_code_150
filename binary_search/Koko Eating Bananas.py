import math
from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    """t O(n + (log m * piles)) / s O(1) """
    left, right = 1, max(piles)
    res = right
    while left <= right:
        mid = (left + right) // 2
        hrs = sum(math.ceil(pile / mid) for pile in piles)

        if hrs <= h:
            res = min(res, mid)
            right = mid - 1
        else:
            left = mid + 1

    return res


if __name__ == '__main__':
    # print(minEatingSpeed(piles=[3, 6, 7, 11], h=8))
    # print(minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))
    print(minEatingSpeed(piles=[312884470], h=312884469))
