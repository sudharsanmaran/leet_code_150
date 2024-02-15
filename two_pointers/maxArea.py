from typing import List


def maxArea(height: List[int]) -> int:
    """t O(n^2) / s O(1)"""
    max_area, length = 0, len(height)
    for i in range(length):
        for j in range(i + 1, length):
            area = (min(height[i], height[j])) * (j - 1)
            max_area = max(max_area, area)

    return max_area


def _max_area(height: List[int]) -> int:
    """t O(n) / s O(1)"""
    left, right, max_area = 0, len(height) - 1, 0
    while left < right:
        area = (min(height[left], height[right])) * (right - left)
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


def maxArea_1(self, height: List[int]) -> int:
    p1, p2, ma = 0, len(height) - 1, 0
    while p1 < p2:
        ma = max(ma, (min(height[p1], height[p2]) * (p2 - p1)))
        if height[p1] <= height[p2]:
            p1 += 1
        else:
            p2 -= 1
    return ma


if __name__ == "__main__":
    print(_max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
