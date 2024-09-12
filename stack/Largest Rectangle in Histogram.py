from collections import deque
from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    """t O(n^2 + n) / s O(n + n)"""
    length = len(heights)
    right_bound, left_bound = [0] * length, [0] * length

    # find possible right index
    for i in range(length):
        if i == length - 1:
            right_bound[i] = i
        for j in range(i + 1, length):
            if heights[i] > heights[j]:
                right_bound[i] = j - 1
                break
            elif j == length - 1:
                right_bound[i] = j

    for i in range(length - 1, -1, -1):
        if i == 0:
            left_bound[i] = i
        for j in range(i - 1, -1, -1):
            if heights[i] > heights[j]:
                left_bound[i] = j + 1
                break
            elif j == 0:
                left_bound[i] = j
    max_area = 0
    for height, l_b, r_b in zip(heights, left_bound, right_bound):
        max_area = max(max_area, (r_b + 1 - l_b) * height)
    return max_area


def largest_rectangle_area(heights: List[int]) -> int:
    """use monotonic stack to find largest or smallest element
    t O(n + n + n) / s O(n + n)"""
    length = len(heights)
    right_bound = [length - 1] * length
    stack = []
    for i in range(length):
        while stack and heights[i] < heights[stack[-1]]:
            popped_index = stack.pop()
            right_bound[popped_index] = i - 1
        stack.append(i)

    left_bound = [0] * length
    stack = []
    for i in range(length - 1, -1, -1):
        while stack and heights[i] < heights[stack[-1]]:
            popped_index = stack.pop()
            left_bound[popped_index] = i + 1
        stack.append(i)
    max_area = 0
    for height, l_b, r_b in zip(heights, left_bound, right_bound):
        max_area = max(max_area, (r_b + 1 - l_b) * height)
    return max_area


def largest_rectangle_area_1(heights: List[int]) -> int:
    """t O(n) / s O(n)"""
    stack, max_area = [], 0
    for index, height in enumerate(heights):
        start = index  # to note left bound as well
        while stack and height < stack[-1][1]:
            idx, ht = stack.pop()
            max_area = max(max_area, (index - idx) * ht)
            start = idx
        stack.append((start, height))

    length = len(heights)  # for remaining elements in stack
    for index, height in stack:
        max_area = max(max_area, (length - index) * height)
    return max_area


def largest_rectangle_area_2(heights: List[int]) -> int:
    stack, max_area, length = [], 0, len(heights)
    for end, height in enumerate(heights):
        start = end
        while stack and stack[-1][1] > height:
            st, ht = stack.pop()
            max_area = max(max_area, (ht * (end - st)))
            start = st
        stack.append((start, height))
    for st, ht in stack:
        max_area = max(max_area, (ht * (length - st)))
    return max_area


if __name__ == "__main__":
    print(largest_rectangle_area_2(heights=[2, 1, 5, 6, 2, 3]))
    # print(largest_rectangle_area_1(heights=[3,6,5,7,4,8,1,0]))
