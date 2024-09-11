from collections import Counter, deque
import heapq
from typing import List


def leastInterval(tasks: List[str], n: int) -> int:
    counter = Counter(tasks)
    tasks = [-count for count in counter.values()]
    heapq.heapify(tasks)
    queue = deque()
    time = 0

    while tasks or queue:
        time += 1
        if queue and queue[0][1] == time:
            heapq.heappush(tasks, queue.popleft()[0])
        if tasks and (task := heapq.heappop(tasks) + 1):
            queue.append((task, time + n))
    return time


assert leastInterval(["A", "A", "A", "B", "B", "B"], n=2) == 8
assert leastInterval(["A", "C", "A", "B", "D", "B"], n=1) == 6
assert leastInterval(["A", "A", "A", "B", "B", "B"], n=3) == 10
