from collections import deque
import time
from typing import List


def solve(board: List[List[str]]) -> None:

    def dfs() -> bool:
        while queue:
            row, col = queue.popleft()
            for adj_row, adj_col in [
                (row, col - 1),
                (row - 1, col),
                (row, col + 1),
                (row + 1, col),
            ]:
                if (adj_row, adj_col) not in visited and board[adj_row][
                    adj_col
                ] != "X":
                    if (adj_row == 0 or adj_row == rows - 1) or (
                        adj_col == 0 or adj_col == cols - 1
                    ):
                        return False
                    visited.add((adj_row, adj_col))
                    queue.append((adj_row, adj_col))
        return True

    rows, cols = len(board), len(board[0])
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if board[row][col] == "O":
                queue = deque([(row, col)])
                visited = set()
                visited.add((row, col))
                if dfs():
                    for _row, _col in visited:
                        board[_row][_col] = "X"
    return board






board = [
    ["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"],
    ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "O", "X", "X", "X", "X", "X"],
    ["X", "O", "X", "X", "X", "O", "X", "X", "X", "O"],
    ["O", "X", "X", "X", "O", "X", "O", "X", "O", "X"],
    ["X", "X", "O", "X", "X", "O", "O", "X", "X", "X"],
    ["O", "X", "X", "O", "O", "X", "O", "X", "X", "O"],
    ["O", "X", "X", "X", "X", "X", "O", "X", "X", "X"],
    ["X", "O", "O", "X", "X", "O", "X", "X", "O", "O"],
    ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"],
]
start = time.time()
print(solve(board=board))
print("total time", time.time() - start)
