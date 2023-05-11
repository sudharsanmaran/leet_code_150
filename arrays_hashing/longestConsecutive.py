from typing import List


def longestConsecutive(nums: List[int]) -> int:
    def _count(num: int, count: int, right: bool):
        while num in num_set:
            count += 1
            num_set.remove(num)
            if right:
                num += 1
            else:
                num -= 1
        return count

    num_set, max_count = set(nums), 0
    for num in nums:
        if num not in num_set:
            continue
        num_set.remove(num)
        count = 1
        count = _count(num + 1, count, True)
        count = _count(num - 1, count, False)
        max_count = max(max_count, count)

    return max_count


if __name__ == '__main__':
    print(longestConsecutive(nums=[1, 2, 0, 1]))
