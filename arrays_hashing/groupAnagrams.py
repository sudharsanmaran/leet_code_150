from collections import Counter, defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """t O(n * m * log(m)) / s O(n * m)"""
    groups = {}
    for string in strs:
        sort_string = "".join(sorted(string))
        if sort_string in groups:
            groups[sort_string].append(string)
        else:
            groups[sort_string] = [string]
    return list(groups.values())


def group_anagrams_2(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for string in strs:
        key = "".join(sorted(string))
        groups[key].append(key)
    return groups.values()


if __name__ == "__main__":
    print(group_anagrams_2(["eat", "tea", "tan", "ate", "nat", "bat"]))
