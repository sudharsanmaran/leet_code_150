from typing import List
import heapq


def lastStoneWeight(stones: List[int]) -> int:
    stones = [-stone for stone in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        stone_1, stone_2 = heapq.heappop(stones), heapq.heappop(stones)
        if stone_1 != stone_2:
            heapq.heappush(stones, stone_1 - stone_2)
    return stones[0] * -1 if stones else 0


assert lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
