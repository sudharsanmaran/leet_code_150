from math import sqrt
import heapq
from typing import List


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    def distance_from_origin(co_ordinates: List):
        return sqrt((co_ordinates[0] ** 2 + co_ordinates[1] ** 2))

    distances = [(-distance_from_origin(point), point) for point in points[:k]]
    heapq.heapify(distances)
    for point in points[k:]:
        dist = -distance_from_origin(point)
        if distances[0][0] < dist:
            heapq.heappushpop(distances, (dist, point))
    return [point for _, point in distances]


kClosest([[3, 3], [5, -1], [-2, 4]], k=2) == [[]]
