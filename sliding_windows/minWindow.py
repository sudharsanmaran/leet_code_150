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
    def is_sub_string_statisfied() -> bool:
        nonlocal sub_string_counter
        nonlocal has_sub
        is_it = all([val == 0 for val in sub_string_counter.values()])
        if is_it:
            sub_string_counter = Counter(t)
            has_sub = True
        return is_it

    sub_string_counter,  has_sub = Counter(t), False
    start_idx, min_sub_len, res_idx, has_sub = -1, len(s), [0] * 2, False
    for idx, char in enumerate(s):
        if sub_string_counter[char] > 0:
            if start_idx == -1:
                start_idx = idx
            sub_string_counter[char] -= 1
        if is_sub_string_statisfied():
            cur_len = idx - start_idx
            if min_sub_len > cur_len:
                min_sub_len = cur_len
                res_idx[0] = start_idx
                res_idx[1] = idx
    if has_sub:
        return s[res_idx[0] : res_idx[1] + 1]
    return ""


if __name__ == "__main__":
    print(minWindow_1(s="ADOBECODEBANC", t="ABC"))
    # print(minWindow(s="a", t="a"))
