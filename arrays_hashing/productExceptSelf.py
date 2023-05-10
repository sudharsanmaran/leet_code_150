from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    """t O(n + n + n) / s o(n + n + n)   without division operator"""
    n = len(nums)
    left_products = [1] * n
    right_products = [1] * n
    res = [0] * n

    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]

    for i in range(n):
        res[i] = left_products[i] * right_products[i]
    return res


if __name__ == '__main__':
    print(productExceptSelf(nums=[1, 2, 3, 4]))
