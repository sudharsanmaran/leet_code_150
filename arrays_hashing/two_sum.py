from collections import defaultdict
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """t O(nums + nums) / s O(nums)"""
    index = {}
    for idx, num in enumerate(nums):
        index[num] = idx
    for idx, num in enumerate(nums):
        to_find = target - num
        found = index.get(to_find, None)
        if found and found != idx:
            return [idx, found]
    return


def two_sum_1(nums: List[int], target: int) -> List[int]:
    """t O(nums) / s O(nums)"""
    counter = {}
    for idx, num in enumerate(nums):
        to_find = target - num
        if to_find in counter:
            return [idx, counter.get(to_find)]
        else:
            counter[num] = idx
    return






def twoSum_11(nums: List[int], target: int) -> List[int]:

    """
    edge cases:
    1. num can be duplicate
    2. avoid finding same num twice
    """
    counter = {}
    for idx, num in enumerate(nums):
        if num in counter:
            return [counter[num], idx]
        else:
            counter[target - num] = idx





if __name__ == '__main__':
    print(twoSum_11([3, 3, 4,], 6))
    print(twoSum_11([-1, -2, -3, -4, -5], -8))





        

