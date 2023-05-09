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


if __name__ == '__main__':
    print(two_sum([-1,-2,-3,-4,-5], -8))
