from collections import Counter, deque
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    """initial
    t O(n/k * k) / s(k)"""
    window = Counter(nums[:k])
    res = [max(window)]
    start = 0
    for i, num in enumerate(nums[k:]):
        window[num] += 1
        if window[nums[start]] == 1:
            del window[nums[start]]
        else:
            window[nums[start]] -= 1
        if res[-1] > num and res[-1] in window:
            res.append(res[-1])
        else:
            res.append(max(window))
        start += 1
    return res


""""we can also solve this by using heap or priority queue but that use binary search so t will be O(n log k)"""


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    """use double ended queue to avoid binary search
    t O(nums) / s O(k)"""
    # store indices of element to easily maintain window
    window, res = deque(), []
    for i in range(len(nums)):
        # remove element outside of window
        if window and window[0] <= i - k:
            window.popleft()

        # remove smallest element
        while window and nums[window[-1]] < nums[i]:
            window.pop()

        window.append(i)

        if i >= k - 1:
            res.append(nums[window[0]])
    return res


def max_sliding_window_heap(nums: List[int], k: int) -> List[int]:
    """t O(n * log n(heap operations)) / s O(k(window) + k(passed values))"""


def max_sliding_window_deque(nums: List[int], k: int) -> List[int]:
    """t O(n) / s O(k)"""
    window, result = deque(), []
    for i in range(len(nums)):
        # remove element if window size reached
        if window and window[0] <= i - k:
            window.popleft()
        # iterate and remove smallest element from left side in window
        while window and nums[window[-1]] < nums[i]:
            window.pop()
        # append new element into window
        window.append(i)
        # append max element into ressult list after reaching k limit
        if i >= k - 1:
            result.append(nums[window[0]])
    return result


if __name__ == "__main__":
    print(max_sliding_window_deque(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
    print(max_sliding_window(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
    print(max_sliding_window_deque(nums=[1, -1], k=1))
    print(max_sliding_window_deque(nums=[7, 2, 4], k=2))
