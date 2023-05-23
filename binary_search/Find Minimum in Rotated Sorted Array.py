from typing import List


def findMin(nums: List[int]) -> int:
    left, right, res = 0, len(nums) - 1, float('inf')
    while left <= right:
        if nums[left] < nums[right]:
            return nums[left]
        mid = (left + right) // 2
        res = min(res, nums[mid])
        if nums[left] <= nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return res


def find_min(nums: List[int]) -> int:
    """
    t O(log nums) / s O(1)
    :param nums:
    :return:
    """
    left, right, res = 0, len(nums) - 1, float('inf')
    # single element array
    if not right:
        return nums[right]
    # un altered sorted array
    if nums[left] <= nums[right]:
        return nums[left]

    while left <= right:
        mid = (left + right) // 2
        res = min(res, nums[mid])
        if left == right:
            return res
        # for left sorted subarray
        elif nums[0] < nums[mid + 1] > nums[mid]:
            left = mid + 1
        # for right sorted subarray
        elif nums[0] > nums[mid + 1] > nums[mid]:
            right = mid - 1
        # fully reversed array
        elif nums[0] > nums[mid + 1] < nums[mid]:
            left = mid + 1
    return res


if __name__ == '__main__':
    print(find_min(nums=[3, 1, 2]))
    print(find_min(nums=[3, 4, 5, 1, 2]))
    print(find_min(nums=[0, 1, 2, 3, 4, 5]))
    print(find_min(nums=[7, 6, 5, 4, 3, 2, 1, 0]))
    print(find_min(nums=[2, 1, 0]))
    print(find_min(nums=[2, 1]))
