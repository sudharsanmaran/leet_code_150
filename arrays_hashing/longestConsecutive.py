from collections import Counter
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


def longestConsecutive_1(nums: List[int]) -> int:
    # if it contains duplicates go with counter
    # but look operation in dict is slower then set
    long_seq = 0
    lookup = Counter(nums)
    for num in nums:
        left, right, cont_seq = num - 1, num + 1, 1
        if lookup[left] < 1:
            while lookup[right] > 0:
                lookup[right] -= 1
                cont_seq += 1
                right += 1
        long_seq = max(long_seq, cont_seq)
    return long_seq


if __name__ == "__main__":
    print(longestConsecutive_1(nums=[100, 4, 200, 1, 3, 2, 1]))
