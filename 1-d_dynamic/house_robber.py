from typing import List
import heapq


def rob(nums: List[int]) -> int:
    odd, even = 0, 0
    for idx, money in enumerate(nums):
        if idx % 2 == 0:
            even += money
        else:
            odd += money
    return max(odd, even)


def rob_1(nums: List[int]) -> int:
    length = len(nums)
    if length == 0:
        return 0


    max_money, prev = 0, 0
    for index in range(length):
        cur = max_money + nums[index]
        max_money = max(max_money, prev)
        prev = cur
    return max(max_money, prev)


def rob_2(nums: List[int]) -> int:
    min_heap = []
    prev, length = 0, len(nums)
    for idx, money in enumerate(nums):
        max_money = min_heap[1] if len(min_heap) > 1 else 0
        if length - 1 == idx and min_heap[0] == nums[0]:
            max_money = max_money[0]
        cur = max_money + money
        if prev:
            if len(min_heap) < 2:
                heapq.heappush(min_heap, prev)
            else:
                heapq.heappushpop(min_heap, prev)
        prev = cur


def rob_3(nums):
    if len(nums) == 1:
        return nums[0]
    return max(rob_1(nums[1:]), rob_1(nums[:-1]))


nums = [2, 7, 9, 3, 1]
nums = [2, 3, 2]
nums=[1]
print(rob_3(nums=nums))
