from collections import deque
from typing import List


def islandsAndTreasure(grid: List[List[int]]) -> None:
    # state for dfs
    visited = set()
    queue = deque()

    def adjacent_nodes(row: int, col: int, distance: int) -> list[tuple]:
        return [
            (row, col - 1, distance),
            (row - 1, col, distance),
            (row, col + 1, distance),
            (row + 1, col, distance),
        ]

    def dfs():
        while queue:
            row, col, distance = queue.popleft()
            if (
                -1 < row < rows
                and -1 < col < cols
                and grid[row][col] != -1
                and grid[row][col] != 0
                and (row, col) not in visited
            ):
                grid[row][col] = distance
                visited.add((row, col))
                queue.extend(adjacent_nodes(row, col, distance + 1))

    # find the chest position
    rows, cols = len(grid), len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                queue.extend(adjacent_nodes(row, col, 1))

    return dfs()


grid = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647],
]
islandsAndTreasure(grid)
print(grid)
