from bisect import bisect_left
from typing import List


def search(nums: List[int], target: int) -> int:
    def _search(left: int, right: int) -> int:
        if left > right:
            return -1
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return _search(mid + 1, right)
        else:
            return _search(left, mid - 1)

    return _search(0, len(nums) - 1)


def search_1(nums: List[int], target: int) -> int:
    idx = bisect_left(nums, target) 
    return idx if idx < len(nums) and nums[idx] == target else -1 

if __name__ == '__main__':
    # print(search_1(nums=[-1, 0, 3, 5, 9, 12], target=9))
    print(search_1(nums=[-1, 0, 3, 5, 9, 12], target=2))
    # print(search_1(nums=[-1, 0, 3, 5, 9, 12], target=13))
