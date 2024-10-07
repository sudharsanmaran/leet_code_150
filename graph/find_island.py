from collections import deque
from typing import List


def numIslands(grid: List[List[str]]) -> int:
    visited = set()
    queue = deque()
    no_of_island = 0

    def bfs():
        while queue:
            cur_row, cur_col = queue.popleft()
            neighbors = [
                (cur_row, cur_col - 1),
                (cur_row - 1, cur_col),
                (cur_row, cur_col + 1),
                (cur_row + 1, cur_col),
            ]
            for row, col in neighbors:
                if (
                    -1 < row < len(grid)
                    and -1 < col < len(grid[0])
                    and (row, col) not in visited
                    and grid[row][col] == "1"
                ):
                    visited.add((row, col))
                    queue.append((row, col))

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "1" and (row, col) not in visited:
                visited.add((row, col))
                queue.append((row, col))
                no_of_island += 1
                bfs()

    return no_of_island


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "1"],
]
print(numIslands(grid))
