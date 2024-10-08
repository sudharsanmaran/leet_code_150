from collections import Counter


def minWindow(s: str, t: str) -> str:
    """
    req: checkInclusion.py
    t O(s) / s O(t)
    """

    t_counter, matches, t_len = Counter(t), 0, len(t)
    window = Counter()
    res_index, res_len = [-1, -1], len(s) + 1
    start = 0
    for i, cur_char in enumerate(s):
        # find permutation
        if cur_char in t_counter:
            if t_counter[cur_char] > window[cur_char]:
                matches += 1
            window[cur_char] += 1

        while matches == t_len:
            # update res
            if res_len > i - start + 1:
                res_index = [start, i + 1]
                res_len = i - start + 1

            # pop element from left
            if s[start] in t_counter:
                if window[s[start]] <= t_counter[s[start]]:
                    matches -= 1
                window[s[start]] -= 1

            start += 1

    return s[res_index[0] : res_index[1]]


def minWindow_1(s: str, t: str) -> str:
    t_counter, window_counter, min_window_size, matches, left, start, end, min_len = (
        Counter(t),
        Counter(),
        len(t),
        0,
        0,
        -1,
        -1,
        len(s) + 1,
    )
    for right, char in enumerate(s):
        window_counter[char] += 1
        if window_counter[char] <= t_counter[char]:
            matches += 1

        while matches == min_window_size:
            if min_len > right + 1 - left:
                start, end = left, right + 1
                min_len = right + 1 - left

            if window_counter[s[left]] <= t_counter[s[left]]:
                matches -= 1

            window_counter[s[left]] -= 1
            left += 1
    return s[start:end] if min_len else ""


if __name__ == "__main__":
    # print(minWindow_1(s="ADOBECODEBANC", t="ABC"))
    print(minWindow_1(s="a", t="a"))
