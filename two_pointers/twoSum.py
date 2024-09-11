from bisect import bisect_left
from typing import List, Optional


def twoSum(numbers: List[int], target: int) -> List[int]:
    """t O(numbers) / s O(numbers)"""
    counter = {}
    for idx, num in enumerate(numbers, 1):
        to_find = target - num
        if to_find in counter:
            return [counter[to_find], idx]
        else:
            counter[num] = idx
    return


def two_sum(numbers: List[int], target: int) -> List[int]:
    """t O(numbers * log numbers) / s O(1)"""

    def binary_search(left: int, right: int) -> Optional[int]:
        """return index or None"""
        if left > right:
            return None

        mid = left + (left - right) // 2

        if numbers[mid] == to_find:
            return mid
        elif numbers[mid] > to_find:
            return binary_search(left, mid - 1)
        else:
            return binary_search(mid + 1, right)

    for idx, num in enumerate(numbers):
        to_find = target - num
        to_find_idx = binary_search(idx + 1, len(numbers) - 1)
        if to_find_idx:
            return [idx + 1, to_find_idx + 1]
    return


def two_sum_bisect(numbers: List[int], target: int) -> List[int]:
    """t O(numbers * log numbers) / s O(1)"""

    for idx, num in enumerate(numbers):
        to_find = target - num
        to_find_idx = bisect_left(numbers, to_find, idx + 1)
        if 0 < to_find_idx < len(numbers) and numbers[to_find_idx] == to_find:
            return [idx + 1, to_find_idx + 1]


def two_sum_1(numbers: List[int], target: int) -> List[int]:
    """two pointer"""
    """t O(numbers) / s O(1)"""
    left, right = 0, len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1


def two_sum_2(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        if (numbers[left] + numbers[right]) == target:
            return [left + 1, right + 1]
        if (numbers[left] + numbers[right]) < target:
            left += 1
        else:
            right -= 1


def two_sum_3(numbers: List[int], target: int) -> List[int]:
    from bisect import bisect_left
    n = len(numbers)
    for i, num in enumerate(numbers):
        rem = target - num
        idx = bisect_left(numbers, rem, lo=i + 1)
        if idx < n and num + numbers[idx] == target:
            return [i + 1, idx + 1]


if __name__ == "__main__":
    print(two_sum_3(numbers=[5, 25, 75], target=100))
