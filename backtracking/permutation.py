from typing import List


def permute(nums: List[int]) -> List[List[int]]: ...


nums = [1, 2, 3]
permute(nums=nums)


"""
1 2 3 => 1 3 2
2 3 1 => 2 1 3
3 1 2 => 3 2 1

"""
