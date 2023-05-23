from typing import List


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    # empty array
    if left > right:
        return -1
    # single element array
    if left == right:
        if nums[left] == target:
            return left
        else:
            return -1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if left == right:
            return -1

        if nums[0] > target:
            # target in right sorted array
            if nums[mid + 1] > nums[mid] >= nums[0]:
                # in left array
                left = mid + 1
            elif nums[mid + 1] < nums[mid] >= nums[0]:
                # pivot
                left = mid + 1
            else:
                # in right
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

        else:
            # target in left sorted array
            if nums[mid + 1] > nums[mid] >= nums[0]:
                # still mid in left
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid + 1] < nums[mid] >= nums[0]:
                # pivot
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    return -1
            else:
                # in right
                right = mid - 1

    return -1


def search_1(nums: List[int], target: int) -> int:
    """
    1. mid can be either in right or left sub array
    2. if mid in left
            2.1 if target present in left
                decrease right
            else
                increase left
        else
            2.2 if target present in right
                increase left
            else
                decrease right
    3. avoid checking empty and single element array which included in while loop itself

    """

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            # mid in Left subarray
            if nums[left] <= target < nums[mid]:
                # Target is in the left sorted subarray
                right = mid - 1
            else:
                # Target is in the right subarray
                left = mid + 1
        else:
            # mid in Right subarray
            if nums[mid] < target <= nums[right]:
                # Target is in the right sorted subarray
                left = mid + 1
            else:
                # Target is in the left subarray
                right = mid - 1

    return -1


if __name__ == '__main__':
    # print(search_1(nums=[4, 5, 6, 7, 8, 9, 10, 11, 122, 0, 1, 2], target=2))
    # print(search_1(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
    # print(search_1(nums=[1, 2, 3,4, 5], target=5))
    # print(search_1(nums=[6, 7, 8, 9, 1, 2, 3, 4, 5], target=5))
    print(search_1(nums=[], target=51))
