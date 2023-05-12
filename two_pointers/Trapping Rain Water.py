from typing import List


def trap(height: List[int]) -> int:
    pocket, mid, left, right = 0, [], 0, 0
    while True:
        while left < 1:
            left += 1
        right = left + 1
        pocket += min(left, right)
        right += 1


    return


if __name__ == '__main__':
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
