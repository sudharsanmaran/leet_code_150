from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """t O(n * m * log(m)) / s O(n * m)"""
    groups = {}
    for string in strs:
        sort_string = ''.join(sorted(string))
        if sort_string in groups:
            groups[sort_string].append(string)
        else:
            groups[sort_string] = [string]
    return list(groups.values())


if __name__ == '__main__':
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
