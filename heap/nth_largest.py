import heapq
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappushpop(min_heap, num)
    return min_heap[0]


assert findKthLargest([3, 2, 1, 5, 6, 4], k=2) == 5
