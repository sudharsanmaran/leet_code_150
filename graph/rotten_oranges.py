from collections import deque
from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    visited = set()

    def dfs():
        total_mins = 0

        while queue:
            row, col, mins = queue.popleft()
            if (
                -1 < row < rows
                and -1 < col < cols
                and grid[row][col]
                and grid[row][col] != 2
                and (row, col) not in visited
            ):
                grid[row][col] = 2
                total_mins = max(mins, total_mins)
                visited.add((row, col))
                queue.extend(get_adjacent_nodes(row, col, mins + 1))
        return total_mins

    def get_adjacent_nodes(row, col, mins):
        return [
            (row, col - 1, mins),
            (row - 1, col, mins),
            (row, col + 1, mins),
            (row + 1, col, mins),
        ]

    # find rotten oranges
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                queue.extend(get_adjacent_nodes(row, col, 1))

    total_mins = dfs()

    # check for un rotten oranges
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                return -1

    return total_mins


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(orangesRotting(grid=grid))
