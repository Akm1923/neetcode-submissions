class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)

        for i in range(n):
            seen = set()

            for j in range(i + 1, n):
                diff = -(nums[i] + nums[j])

                if diff in seen:
                    triplet = tuple(sorted([nums[i], nums[j], diff]))
                    ans.add(triplet)

                seen.add(nums[j])

        return [list(triplet) for triplet in ans]