class Solution:
    def __init__(self):
            self.res=[]
    def f(self,nums,o,t,idx):
        if t == 0:
            self.res.append(o[:])
            return

        if t < 0 or idx == len(nums):
            return
        o.append(nums[idx])
        self.f(nums,o,t-nums[idx],idx)
        o.pop()
        self.f(nums,o,t,idx+1)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.f(nums,[],target,0)
        return self.res


        