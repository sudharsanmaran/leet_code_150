import time
from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    def backtrack(start, cur_sum, cur_candidates):
        if cur_sum == target:
            res.append(cur_candidates[:])
            return
        elif cur_sum > target:
            return

        for i in range(start, len(candidates)):
            cur_candidate = candidates[i]
            if cur_candidate + cur_sum > target:
                break
            cur_candidates.append(cur_candidate)
            backtrack(start, cur_sum + cur_candidate, cur_candidates)
            start += 1
            cur_candidates.pop()

    res = []
    candidates.sort()
    backtrack(0, 0, [])
    return res


st = time.time()
candidates = [2, 3, 5]
target = 8
print(combinationSum(candidates=candidates, target=target))
print("total_time", time.time() - st)
