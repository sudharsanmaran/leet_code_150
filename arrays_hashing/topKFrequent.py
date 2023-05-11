from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """t O(n * n * log(n)) / s O(n)"""
    from collections import Counter
    counter = Counter(nums)
    return [num for num, _ in counter.most_common(k)]


def top_k_frequent_1(nums: List[int], k: int) -> List[int]:
    """t O(n * n * log(n)) / s O(n)"""
    counter = {}
    for num in nums:
        counter[num] = 1 + counter.get(num, 0)
    return [num for num, _ in sorted(counter.items(), key=lambda x: x[1], reverse=True)[:k]]


def top_k_frequent_2(nums: List[int], k: int) -> List[int]:
    """used heap instead of sorting"""
    """t O(n * k log(k)) / s O(n + k)"""
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1
    import heapq
    heap = []
    for num, count in counter.items():
        if len(heap) < k:
            heapq.heappush(heap, (count, num))
        else:
            heapq.heappushpop(heap, (count, num))

    return [num for count, num in heap]


if __name__ == '__main__':
    print(top_k_frequent_2(nums=[1, 1, 1, 2, 2, 3, 5, 5], k=2))
