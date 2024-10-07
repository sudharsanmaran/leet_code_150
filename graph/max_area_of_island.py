from collections import deque
from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    visited = set()
    queue = deque()
    max_area = 0

    def get_area() -> int:
        area = 1
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
                    and grid[row][col] == 1
                ):
                    area += 1
                    visited.add((row, col))
                    queue.append((row, col))
        return area

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1 and (row, col) not in visited:
                visited.add((row, col))
                queue.append((row, col))
                max_area = max(get_area(), max_area)
    return max_area


grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]
print(maxAreaOfIsland(grid))
