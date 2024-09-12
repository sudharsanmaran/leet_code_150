from collections import Counter


def is_anagram_1(s: str, t: str) -> bool:
    """t O(s + t) / s O(s)"""
    if len(s) != len(t):
        return False
    counter = Counter(s)
    for char in t:
        if char not in counter or counter[char] == 0:
            return False
        counter[char] -= 1

    return True


def is_anagram_2(s: str, t: str) -> bool:
    """t O(s log s + t log t)/ s O(1)"""
    return sorted(s) == sorted(t)










def is_anagram_3(s: str, t: str) -> bool:

    """O(n + n) / O(n)"""
    if len(s) != len(t):
        return False
    
    s_counter = Counter(s)
    for char in t:
        if s_counter[char] < 1:
            return False
        s_counter[char] -= 1
        
    return True
        



print(is_anagram_3(s='anagram', t='maranag'))