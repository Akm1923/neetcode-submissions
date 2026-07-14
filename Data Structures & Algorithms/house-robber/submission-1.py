class Solution:
    def sol(self,nums,idx,dp):
        if idx>=len(nums):
            return 0
        if dp[idx]!=-1:
            return dp[idx]
        take=nums[idx]+self.sol(nums,idx+2,dp)
        not_take=self.sol(nums,idx+1,dp)
        dp[idx]=max(take,not_take)
        return dp[idx]
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*(n+1)
        return self.sol(nums,0,dp)


        