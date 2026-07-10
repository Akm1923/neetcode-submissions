class Solution:
    def __init__(self):
        self.res=[]
    def f(self,idx,n,o,nums):
        if idx>=n:
            self.res.append(o[:]) 
            return 

        o.append(nums[idx])
        self.f(idx+1,n,o,nums)
        o.pop()
        self.f(idx+1,n,o,nums)

        return self.res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        o=[]
        return self.f(0,len(nums),o,nums)