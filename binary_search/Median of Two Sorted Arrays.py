import bisect
from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    """ t O(nums2 * log(nums1) / s O(1)"""
    for num in nums2:
        bisect.insort_left(nums1, num)
    length = len(nums1)
    if length % 2 == 1:
        return nums1[length // 2]
    else:
        mid_r = length // 2
        mid_l = mid_r - 1
        return (nums1[mid_l] + nums1[mid_r]) / 2


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """t O(n + m)/ s O(n + m)"""
    nums = []
    nums1_len, nums2_len, i, j = len(nums1), len(nums2), 0, 0
    while i < nums1_len and j < nums2_len:
        if nums1[i] <= nums2[j]:
            nums.append(nums1[i])
            i += 1
        else:
            nums.append(nums2[j])
            j += 1
    #  remaining
    nums.extend(nums1[i:])
    nums.extend(nums2[j:])
    # median
    length = len(nums)
    if length % 2 == 1:
        return nums[length // 2]
    else:
        mid_r = length // 2
        mid_l = mid_r - 1
        return (nums[mid_l] + nums[mid_r]) / 2


def find_median_sorted_arrays_1(nums1: List[int], nums2: List[int]) -> float:
    """
    1. to find median need to split array into two parts in sorted order
    1.1. using binary search to split array into two parts efficiently
    t O(log(m + n)) / t O(1)
    """
    n, m = len(nums1), len(nums2)
    if n > m:  # to avoid index error at  part_2 = (n + m + 1) // 2 - part_1
        nums1, nums2 = nums2, nums1
        n, m = m, n

    left, right = 0, n
    while left <= right:
        part_1 = (left + right) // 2
        part_2 = (n + m + 1) // 2 - part_1

        part_1_min = float('-inf') if part_1 == 0 else nums1[part_1 - 1]
        part_1_max = float('inf') if part_1 == n else nums1[part_1]

        part_2_min = float('-inf') if part_2 == 0 else nums2[part_2 - 1]
        part_2_max = float('inf') if part_2 == m else nums2[part_2]

        if part_1_min <= part_2_max and part_2_min <= part_1_max:
            if (n + m) % 2 == 0:
                return (max(part_1_min, part_2_min) + min(part_2_max, part_1_max)) / 2
            else:
                return max(part_1_min, part_2_min)
        elif part_1_min > part_2_max:
            right = part_1 - 1
        else:
            left = part_1 + 1


if __name__ == '__main__':
    # print(find_median_sorted_arrays_1(nums1=[1, 3, 6], nums2=[2, 4, 7]))  # 1, 2, 3, 4, 6, 7, 8
    # print(find_median_sorted_arrays_1(nums1=[1, 3], nums2=[2]))
    print(find_median_sorted_arrays_1(nums1=[0, 0], nums2=[0, 0]))
