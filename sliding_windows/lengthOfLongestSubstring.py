def lengthOfLongestSubstring(s: str) -> int:
    """t O(n) / s O(n)"""
    start, sub_str, max_len = 0, set(), 0
    for end, char in enumerate(s):
        while char in sub_str:
            sub_str.remove(s[start])
            start += 1
        sub_str.add(char)
        max_len = max(max_len, end - start + 1)
    return max_len


if __name__ == '__main__':
    print(lengthOfLongestSubstring(s="pwwkew"))
