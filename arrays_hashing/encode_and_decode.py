from typing import List


def encode(strings: List[str]) -> str:
    res = ''
    for string in strings:
        res += f'{len(string)}#'
        for char in string:
            res += chr(ord(char) + 3)
    return res


def decode(string: str) -> List[str]:
    res, n, idx = [], len(string), 0
    while idx < n:
        hash_index = string.index('#', idx)
        length = int(string[idx: hash_index])
        string_start_index = hash_index + 1
        string_end_index = hash_index + 1 + length
        dec_string = ''.join(chr(ord(i) - 3) for i in string[string_start_index: string_end_index])
        res.append(dec_string)
        idx = string_end_index
    return res


if __name__ == '__main__':
    print(decode(encode(['hihellofdg', 'areg,.;ds', '#testzZ~'])))
