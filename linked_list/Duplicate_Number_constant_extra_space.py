from typing import List


def findDuplicate(nums: List[int]) -> int:
    """floyd's detection algo cuz we know nums must be in range(n) and it has n + 1 elements means exactly one duplicate
     allowed
     t O(n) / s O(1)"""
    slow, fast = 0, 0
    while True:
        # if we have range(n) then every element can be index of next subsequent element
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow


if __name__ == '__main__':
    print(findDuplicate(nums=[1, 2, 3, 4, 5, 6, 5]))
