from collections import Counter


def checkInclusion(s1: str, s2: str) -> bool:
    """t O(s2 + (s1 * (s2/s1)) / O(s1 + s1)"""
    s1_counter = Counter(s1)
    window = Counter(s2[: len(s1)])

    if s1_counter == window:
        return True

    start = 0
    for end in s2[len(s1) :]:
        window.update(end)
        window[s2[start]] -= 1

        if s1_counter == window:
            return True

        start += 1

    return False


def check_inclusion(s1: str, s2: str) -> bool:
    """maintain auxiliary variable 'matches' to avoid checking hashmap in every iteration"""
    """t O(s2) / s O(s1 + s1)"""
    window = len(s1)

    s1_counter, window_counter = {}, {}
    for char in s1:
        s1_counter[char] = 1 + s1_counter.get(char, 0)

    matches = 0
    for i, cur_char in enumerate(s2):
        if cur_char in s1_counter:
            if window_counter.get(cur_char, 0) >= s1_counter[cur_char]:
                matches -= 1
            else:
                matches += 1
            window_counter[cur_char] = 1 + window_counter.get(cur_char, 0)

        if i >= window:
            leftmost_char = s2[i - window]
            if leftmost_char in s1_counter:
                if s1_counter[leftmost_char] >= window_counter[leftmost_char]:
                    matches -= 1
                else:
                    matches += 1
                window_counter[leftmost_char] -= 1

        if matches == window:
            return True

    return False


def check_inclusion_1(s1: str, s2: str) -> bool:
    left, counter, window_size, total_size = 0, Counter(s1), len(s1), len(s2)
    cur_window_counter, right = Counter(s2[:window_size]), window_size
    while right < total_size:
        if counter == cur_window_counter:
            return True
        else:
            cur_window_counter[s2[left]] -= 1
            left += 1
            cur_window_counter.update(s2[right])
            right += 1
    if counter == cur_window_counter:
        return True
    return False


def check_inclusion_2(s1: str, s2: str) -> bool:
    s1_counter, window_counter, window_size, matches, left = (
        Counter(s1),
        Counter(),
        len(s1),
        0,
        0,
    )
    for right, char in enumerate(s2):
        window_counter[char] += 1
        if window_counter[char] <= s1_counter[char]:
            matches += 1

        if right - left + 1 > window_size:
            left_char = s2[left]
            if window_counter[left_char] <= s1_counter[left_char]:
                matches -= 1
            window_counter[left_char] -= 1
            left += 1

        if matches == window_size:
            return True
    return False


if __name__ == "__main__":
    # print(check_inclusion_2(s1="adc", s2="dcda"))
    # print(check_inclusion_2(s1="abc", s2="eidbacooo"))
    # print(check_inclusion_2(s1="adc", s2="dcda"))
    print(check_inclusion_2(s1="qff", s2="ifisnoskikfqzrmzlv"))
    print(check_inclusion_2(s1="abcdxabcde", s2="abcdxabcde"))
    print(
        check_inclusion_2(
            s1="trinitrophenylmethylnitramine",
            s2="dinitrophenylhydrazinetrinitrophenylmethylnitramine",
        )
    )
