from typing import List

# from binary_search.search import search


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    """t O(log m + log n) / s O(1)"""

    def _search_matrix(left: int, right: int) -> bool:
        if left > right:
            return False

        mid = (left + right) // 2

        if left == right:
            return search(matrix[mid], target=target) > 0

        elif target < matrix[mid][0]:
            return _search_matrix(left, mid - 1)
        else:
            return _search_matrix(mid + 1, right)

    return _search_matrix(0, len(matrix))


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    left, right = 0, len(matrix) - 1
    while left <= right:
        row_mid = (left + right) // 2

        if target > matrix[row_mid][-1]:
            left = row_mid + 1
        elif target < matrix[row_mid][0]:
            right = row_mid - 1
        else:
            break

    if left > right:
        return False

    row = (left + right) // 2
    left, right = 0, len(matrix[row]) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == matrix[row][mid]:
            return True
        elif target < matrix[row][mid]:
            right = mid - 1
        else:
            left = mid + 1

    return False


def search_mat(matrix: List[List[int]], target: int) -> bool:
    def _find_target(left, right, row: int):
        if left > right:
            return False
        mid = (left + right) // 2
        if matrix[row][mid] == target:
            return True
        elif matrix[row][mid] < target:
            _find_target(left + 1, right)
        else:
            _find_target(left, right + 1)

    def _find_row(left, right):
        mid = (left + right) // 2
        if matrix[mid][0] < target:
            _find_row(mid + 1, right)
        elif matrix[mid][-1] > target:
            _find_row(left, mid - 1)
        else:
            return mid
    row = _find_row(0, len(matrix))
    _find_target(0, len(matrix[row]), row)


if __name__ == "__main__":
    print(
        search_mat(
            matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=20
        )
    )
    print(search_matrix(matrix=[[1]], target=1))
