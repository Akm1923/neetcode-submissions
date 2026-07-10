from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        used = [False] * len(nums)

        def dfs(path):
            if len(path) == len(nums):
                self.res.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # Choose
                used[i] = True
                path.append(nums[i])

                dfs(path)

                # Backtrack
                path.pop()
                used[i] = False

        dfs([])
        return self.res