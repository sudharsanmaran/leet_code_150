from collections import deque
from typing import List


def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:

    def dfs(row, col) -> bool:
        visited = set()
        queue = deque([(row, col)])
        while queue:
            row, col = queue.popleft()
            for adj_row, adj_col in [
                (row, col - 1),
                (row - 1, col),
                (row, col + 1),
                (row + 1, col),
            ]:
                if (
                    -1 < adj_row < rows
                    and -1 < adj_col < cols
                    and (adj_row, adj_col) not in visited
                    and heights[row][col] >= heights[adj_row][adj_col]
                ):
                    update_boundary(adj_row, adj_col)
                    if state["atlantic"] and state["pacific"]:
                        return True
                    visited.add((adj_row, adj_col))
                    queue.append((adj_row, adj_col))
        return False

    def update_boundary(row, col) -> None:
        if row == 0 or col == 0:
            state["pacific"] = True
        if row == rows - 1 or col == cols - 1:
            state["atlantic"] = True

    res = []
    rows, cols = len(heights), len(heights[0])
    for row in range(rows):
        for col in range(cols):
            state = {"pacific": False, "atlantic": False}
            update_boundary(row, col)
            if state["pacific"] and state["atlantic"]:
                res.append([row, col])
            else:
                if dfs(row, col):
                    res.append([row, col])
    return res


def pacificAtlantic_1(heights: List[List[int]]) -> List[List[int]]:
    def dfs(row, col, reachable):
        reachable.add((row, col))
        for adj_row, adj_col in [
            (row, col - 1),
            (row - 1, col),
            (row, col + 1),
            (row + 1, col),
        ]:
            if (
                -1 < adj_row < rows
                and -1 < adj_col < cols
                and (adj_row, adj_col) not in reachable
                and heights[row][col] <= heights[adj_row][adj_col]
            ):
                dfs(adj_row, adj_col, reachable)

    rows, cols = len(heights), len(heights[0])
    pacific_reachable, atlantic_reachable = set(), set()

    for row in range(rows):
        dfs(row, 0, pacific_reachable)
        dfs(row, cols - 1, atlantic_reachable)

    for col in range(cols):
        dfs(0, col, pacific_reachable)
        dfs(rows - 1, col, atlantic_reachable)

    return list(pacific_reachable & atlantic_reachable)


heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]
print(pacificAtlantic_1(heights=heights))
