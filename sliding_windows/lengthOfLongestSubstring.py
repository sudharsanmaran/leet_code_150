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


def with_dict(s: str) -> int:
    char_index_map, max_len, left, right, n = {}, 0, 0, 0, len(s)
    if n == 1:
        return 1
    while True:
        while right < n and s[right] not in char_index_map:
            char_index_map[s[right]] = right
            right += 1

        max_len = max(max_len, (right - left))
        if right >= n - 1:
            break
        upto_index = char_index_map[s[right]]
        while left <= upto_index:
            del char_index_map[s[left]]
            left += 1
    return max_len


def with_dict_2(s: str) -> int:
    """avoid removal in dict"""
    char_index_map, max_len, left, right, n = {}, 0, 0, 0, len(s)
    while True:
        while s[right] not in char_index_map or char_index_map[s[right]] < left:
            char_index_map[s[right]] = right
            right += 1
            if right == n:
                break

        max_len = max(max_len, right - left)
        if right >= n - 1:
            break
        left = char_index_map[s[right]] + 1

    return max_len


def with_dict_3(s: str) -> int:
    """avoid while true"""
    char_index_map, max_len, left = {}, 0, 0
    for right, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= left:
            left = char_index_map[char] + 1

        char_index_map[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len


if __name__ == "__main__":
    # print(with_dict(s="pwwkew"))
    print(with_dict_3(s="tmmzuxtt"))
    # print(with_dict_3(s="dvdf"))
