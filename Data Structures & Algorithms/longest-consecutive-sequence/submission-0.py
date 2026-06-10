class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=sorted(set(nums))
        m=0
        count=1
        for num in s:
            if num+1 in s:
                count=count+1
            else:
                m=max(count,m)
                count=1
        return m
            
                



        