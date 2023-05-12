from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    """initial approach"""
    """t O(n * m) / s O(less then n * m)"""
    row_counter, col_counter, sq_1, sq_2, sq_3 = {}, {}, {}, {}, {}
    for i in range(9):
        for j in range(9):
            # row
            if row_counter.get(board[i][j], None):
                print(f'row false, i: {i}, j: {j}, value: {board[i][j]}, row_counter: {row_counter}')
                return False
            elif board[i][j] != '.':
                row_counter[board[i][j]] = True

            # col
            if col_counter.get(board[j][i], None):
                print(f'col false, i: {i}, j: {j}, value: {board[i][j]}, col_counter: {col_counter}')
                return False
            elif board[j][i] != '.':
                col_counter[board[j][i]] = True

            # sq_1
            if j < 3 and sq_1.get(board[i][j], None):
                print(f'sq_1 false, i: {i}, j: {j}, value: {board[i][j]}, sq_1: {sq_1}')
                return False
            elif j < 3 and board[i][j] != '.':
                sq_1[board[i][j]] = True

            # sq_2
            if 2 < j < 6 and sq_2.get(board[i][j], None):
                print(f'sq_2 false, i: {i}, j: {j}, value: {board[i][j]}, sq_2: {sq_2}')
                return False
            elif 2 < j < 6 and board[i][j] != '.':
                sq_2[board[i][j]] = True

            # sq_3
            if 5 < j < 9 and sq_3.get(board[i][j], None):
                print(f'sq_3 false, i: {i}, j: {j}, value: {board[i][j]}, sq_3: {sq_3}')
                return False
            elif 5 < j < 9 and board[i][j] != '.':
                sq_3[board[i][j]] = True
        row_counter, col_counter = {}, {}
        if i == 2:
            sq_1, sq_2, sq_3 = {}, {}, {}
        if i == 5:
            sq_1, sq_2, sq_3 = {}, {}, {}
        if i == 8:
            sq_1, sq_2, sq_3 = {}, {}, {}
    return True


def is_valid_sodoku(board: List[List[str]]) -> bool:
    """make counter key diff"""
    """t O(n * m) / s O(n * m)"""
    counter = {}
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == '.':
                continue
            if (i, num) in counter:
                return False
            else:
                counter[(i, num)] = True
            if (num, j) in counter:
                return False
            else:
                counter[(num, j)] = True

            subgrid_key = (i // 3, j // 3, num)
            if subgrid_key in counter:
                return False
            else:
                counter[subgrid_key] = True
    return True


if __name__ == '__main__':
    print(is_valid_sodoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                           [".", "9", "8", ".", ".", ".", ".", "6", "."],
                           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                           [".", "6", ".", ".", ".", ".", "2", "8", "."],
                           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                           [".", "1", ".", ".", "8", ".", "3", "7", "9"]]))
