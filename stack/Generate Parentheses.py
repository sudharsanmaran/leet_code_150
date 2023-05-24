from typing import List


def generateParenthesis(n: int) -> List[str]:
    res = []

    def combination(left, right, s, length):
        if n * 2 == length:
            res.append(s)
            return

        if left < n:
            combination(left + 1, right, s + '(', length + 1)
        if right < left:
            combination(left, right + 1, s + ')', length + 1)

    combination(0, 0, '', 0)
    return res


if __name__ == '__main__':
    print(generateParenthesis(n=3))
