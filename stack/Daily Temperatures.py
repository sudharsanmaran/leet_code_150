from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    """monotonic decreasing stack
    t O(n) / s O(n)"""
    res = [0] * len(temperatures)
    stack = []
    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            idx = stack.pop()
            res[idx] = i - idx
        stack.append(i)
    return res


if __name__ == '__main__':
    dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
