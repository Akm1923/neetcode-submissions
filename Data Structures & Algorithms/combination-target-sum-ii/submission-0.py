from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []

        def dfs(idx, target, path):
            if target == 0:
                self.res.append(path[:])
                return

            if idx == len(candidates) or target < 0:
                return

            # Take
            path.append(candidates[idx])
            dfs(idx + 1, target - candidates[idx], path)
            path.pop()

            # Not Take
            next_idx = idx + 1
            while next_idx < len(candidates) and candidates[next_idx] == candidates[idx]:
                next_idx += 1

            dfs(next_idx, target, path)

        dfs(0, target, [])
        return self.res