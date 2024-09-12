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


def dailyTemperatures_1(temperatures: List[int]) -> List[int]:
    result, stack = [0] * len(temperatures), []
    for idx, num in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < num:
            i = stack.pop()
            result[i] = idx - i
        stack.append(idx)
    return result


if __name__ == '__main__':
    print(dailyTemperatures_1([73, 74, 75, 71, 69, 72, 76, 73]))
