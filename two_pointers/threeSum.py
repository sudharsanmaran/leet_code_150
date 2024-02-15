from bisect import insort_left
from collections import Counter
from typing import List


def naive_3_sum(nums: List[int]) -> List[List[int]]:
    """t O(n ^ 3) / s O(result)"""
    n, res_dict = len(nums), {}
    res = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    key = tuple(sorted([nums[i], nums[j], nums[k]]))
                    if key not in res_dict:
                        res.append([nums[i], nums[j], nums[k]])
                        res_dict[key] = True
    return res


def threeSum(nums: List[int]) -> List[List[int]]:
    """t O(n ^ 2) / s O(n + result)"""
    counter = Counter(nums)
    n, res, res_set = len(nums), [], set()
    for i in range(n):
        counter[nums[i]] -= 1
        for j in range(i + 1, n):
            temp = []
            counter[nums[j]] -= 1
            insort_left(temp, nums[i])
            insort_left(temp, nums[j])
            rem = -(nums[i] + nums[j])
            if rem in counter and counter[rem] > 0:
                insort_left(temp, rem)
                temp_tpl = tuple(temp)
                if temp_tpl not in res_set:
                    res.append([nums[i], nums[j], rem])
                    res_set.add(temp_tpl)
            counter[nums[j]] += 1
        counter[nums[i]] += 1

    return res


def _three_sum(nums: List[int]) -> List[List[int]]:
    """t O(n^2) / s O(1)"""
    nums.sort()
    res, n = [], len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = n - 1
        while left < right:
            cur_sum = nums[i] + nums[left] + nums[right]
            if cur_sum == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif cur_sum < 0:
                left += 1
            else:
                right -= 1
    return res


def threeSum_1(nums: List[int]) -> List[List[int]]:
    def is_prsent(num: int) -> bool:
        if counter[num] > 0:
            counter[num] -= 1
            return True
        return False

    counter = Counter(nums)
    left, right, output = 0, len(nums) - 1, []
    nums.sort()
    while left < right:
        rem = (nums[left] + nums[right]) * -1
        if is_prsent(rem) and is_prsent(nums[left]) > 0 and is_prsent(nums[right]) > 0:
            output.append([rem, nums[left], nums[right]])
        if rem < 0:
            left += 1
        else:
            right -= 1
    return output


if __name__ == "__main__":
    print(threeSum_1([-1, 0, 1, 2, -1, -4]))
