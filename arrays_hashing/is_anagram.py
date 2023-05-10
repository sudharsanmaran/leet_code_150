def is_anagram_1(s: str, t: str) -> bool:
    """t O(n) / s O(s)"""
    if len(s) != len(t):
        return False
    from collections import Counter
    counter = Counter(s)
    for char in t:
        if char not in counter or counter[char] == 0:
            return False
        counter[char] -= 1
    for count in counter.values():
        if count != 0:
            return False
    return True


def is_anagram_2(s: str, t: str) -> bool:
    """t O(n log n)/ s O(1)"""
    return sorted(s) == sorted(t)
