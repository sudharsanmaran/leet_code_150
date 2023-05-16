from collections import Counter


def checkInclusion(s1: str, s2: str) -> bool:
    """t O(s2) / O(s1 + s1)"""
    s2_counter = Counter(s1)
    window = Counter(s2[:len(s1)])

    if s2_counter == window:
        return True

    start = 0
    for end in s2[len(s1):]:
        window.update(end)
        window[s2[start]] -= 1

        if s2_counter == window:
            return True

        start += 1

    return False


if __name__ == '__main__':
    print(checkInclusion(s1="ab", s2="eidbaooo"))
    print(checkInclusion(s1="abc", s2="eidbacooo"))
    print(checkInclusion(s1="adc", s2="dcda"))



