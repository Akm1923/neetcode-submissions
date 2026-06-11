class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        for i in range(0,len(prices)):
            curr_max=0
            r_m=max(prices[i+1:]) if i<len(prices)-1 else 0
            if prices[i]<r_m:
                curr_max=r_m-prices[i]
                m=max(curr_max,m)
        return m
                



        