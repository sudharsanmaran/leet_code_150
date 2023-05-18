from typing import List


def generateParenthesis(n: int) -> List[str]:
    res = []

    def back_track(left, right, s, length):
        if n * 2 == length:
            res.append(s)
            return

        if left < n:
            back_track(left + 1, right, s + '(', length + 1)
        if right < left:
            back_track(left, right + 1, s + ')', length + 1)

    back_track(0, 0, '', 0)
    return res


if __name__ == '__main__':
    print(generateParenthesis(n=3))
