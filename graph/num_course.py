from collections import defaultdict, deque
from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    pre_map = defaultdict(set)
    completed, visited = set(), set()
    queue = deque()
    for courses, prerequire in prerequisites:
        pre_map[courses].add(prerequire)

    def dfs():
        while queue:
            cur_course = queue.popleft()
            if cur_course not in completed:
                if cur_course not in visited:
                    if cur_course in pre_map:
                        if rem := pre_map[cur_course] - completed:
                            queue.extend(rem)
                            queue.append(cur_course)
                        else:
                            completed.add(cur_course)
                    else:
                        completed.add(cur_course)
                    visited.add(cur_course)
                else:
                    completed.add(cur_course)

    for course in pre_map:
        queue.append(course)
        dfs()

    return len(queue) == 0


numCourses = 2
prerequisites = [[1, 0], [2, 1], [2, 3]]
assert canFinish(numCourses, prerequisites) == False
