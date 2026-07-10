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
        next_idx=idx+1
        while next_idx < n and nums[next_idx] == nums[idx]:
            next_idx += 1

        self.f(next_idx,n,o,nums)

        return self.res

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.f(0,len(nums),[],nums)
        return self.res
        
        