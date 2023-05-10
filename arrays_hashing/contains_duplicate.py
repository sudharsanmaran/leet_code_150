from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    counter = {}
    for num in nums:
        if num in counter:
            return True
        else:
            counter[num] = True
    return False
