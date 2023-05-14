from typing import List, Tuple


def trap(height: List[int]) -> int:
    """initial approach incomplete"""
    left, right, total_pocket, length = 0, 0, 0, len(height)

    def get_pockets(idx: int) -> Tuple[int, int]:
        _pocket, lft = 0, idx - 1
        while height[idx] < height[lft]:
            _pocket += height[lft] - height[idx]
            idx += 1
            if idx + 1 == length:
                return -1, 0
        return idx, _pocket

    while left < length - 1:
        while left == 0 and height[left] < 1:
            left += 1
        right, pocket = get_pockets(left + 1)
        total_pocket += pocket
        if right > 0:
            left = right
        else:
            left += 1
    return total_pocket


def trap_water(height: List[int]) -> int:
    """t O(n) / s O(1)"""
    n = len(height)
    left, right, left_max, right_max, pockets = 0, n - 1, 0, 0, 0
    while left < right:
        if height[left] <= height[right]:
            left_max = max(left_max, height[left])
            pockets += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            pockets += right_max - height[right]
            right -= 1

    return pockets


if __name__ == '__main__':
    print(trap_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
