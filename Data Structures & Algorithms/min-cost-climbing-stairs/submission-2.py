class Solution:
    def sol(self,cost,idx,n,dp):
        if idx>n-1:
            return 0
        if idx==n-1:
            return cost[n-1]
        if dp[idx]!=-1:
            return dp[idx]
        one=cost[idx]+self.sol(cost,idx+1,n,dp)
        two=cost[idx]+self.sol(cost,idx+2,n,dp)
        dp[idx]=min(one,two)
        return dp[idx]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        idx=0
        dp=[-1]*(n+1)
        dp[n-1]=cost[n-1]
        
        return min(self.sol(cost,0,n,dp),self.sol(cost,1,n,dp))


        
        