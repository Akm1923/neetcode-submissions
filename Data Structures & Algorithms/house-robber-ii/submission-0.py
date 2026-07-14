class Solution:
    def sol(self,nu,idx,dp):
        if idx>=len(nu):
            return 0
        if dp[idx]!=-1:
            return dp[idx]
        take=nu[idx]+self.sol(nu,idx+2,dp)
        not_take=self.sol(nu,idx+1,dp)
        dp[idx]=max(take,not_take)
        return dp[idx]
        
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]

        dp1=[-1]*(n+1)
        dp2=[-1]*(n+1)
        return max(self.sol(nums[:n-1],0,dp1),self.sol(nums[1:n],0,dp2))

        