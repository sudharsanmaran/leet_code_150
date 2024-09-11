import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = nums[:k]
        heapq.heapify(self.stream)
        for num in nums[k:]:
            if num > self.stream[0]:
                heapq.heappushpop(self.stream, num)

    def add(self, val: int) -> int:
        if len(self.stream) < self.k:
            heapq.heappush(self.stream, val)
        elif val > self.stream[0]:
            heapq.heappushpop(self.stream, val)
        return self.stream[0]


obj = KthLargest(3, [1, 2, 3, 3])
assert obj.add(3) == 3
assert obj.add(5) == 3
assert obj.add(6) == 3
assert obj.add(7) == 5
assert obj.add(8) == 6
