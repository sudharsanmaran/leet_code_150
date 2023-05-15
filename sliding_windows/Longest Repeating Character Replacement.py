from collections import Counter


def characterReplacement(s: str, k: int) -> int:
    """t O(n) / O(1)"""
    """need fix: have to find which is less frequent to replace it"""
    start, max_same_chars, same_chars = 0, 0, 1
    for end in range(start + 1, len(s)):
        if s[start] == s[end]:
            same_chars += 1
            max_same_chars = max(max_same_chars, same_chars)
        elif k > 0:
            same_chars += 1
            k -= 1
            max_same_chars = max(max_same_chars, same_chars)
        else:
            start, same_chars = end, 1
    return max_same_chars


def character_replacement(s: str, k: int) -> int:
    """O(n + n * log n)/ O(n)"""
    """incomplete fail's test case"""

    def is_possible(char) -> bool:
        arr = valid_str.most_common()
        if arr[1:]:
            pos = sum(count for _, count in arr[1:])
            if char not in arr[0]:
                pos += 1
            if pos > k:
                return False
        elif k == 0 and valid_str and arr[0][1] > 0 and char not in valid_str:
            return False
        return True

    start, i, valid_str, max_count = 0, 0, Counter(), 0
    while i < len(s):
        if is_possible(s[i]):
            valid_str.update(s[i])
            max_count = max(max_count, sum(count for _, count in valid_str.most_common()))
            i += 1
        else:
            valid_str[s[start]] -= 1
            start += 1
    max_count += (k - sum(count for _, count in valid_str.most_common()[1:]))
    return max_count


def character_replacement_1(s: str, k: int) -> int:
    """there is only 26 possible capital characters so n * 26 is better then n * log n i.e traversal is better
    then sorting"""
    """t O(26 * n) / s O(n)"""
    start, counter, res = 0, {}, 0
    for end, char in enumerate(s):
        counter[char] = 1 + counter.get(char, 0)

        while (end - start - max(counter.values())) > k:
            counter[s[start]] -= 1
            start += 1

        res = max(res, end - start + 1)
    return res


def character_replacement_2(s: str, k: int) -> int:
    """still we are adding element to hashmap we can maintain most frequent element"""
    """t O(n) / s O(s)"""
    start, counter, res, mostf = 0, {}, 0, 0
    for end, char in enumerate(s):
        counter[char] = 1 + counter.get(char, 0)
        mostf = max(mostf, counter[char])

        while (end - start - mostf) > k:
            counter[s[start]] -= 1
            start += 1

        res = max(res, end - start + 1)
    return res


if __name__ == '__main__':
    print(character_replacement_1(s="AABABBA", k=1))
    print(character_replacement_2(s="BAAA", k=0))
    print(character_replacement_2(s="ABCCCCC", k=2))
    print(character_replacement_2(s="AAAA", k=2))
