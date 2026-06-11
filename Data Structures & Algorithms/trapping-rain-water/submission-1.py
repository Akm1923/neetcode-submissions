class Solution:
    def trap(self, height: List[int]) -> int:
        water=0
        l_mh=[max(height[:i]) if i > 0 else 0 for i in range(len(height))]
        r_mh=[max(height[i+1:]) if i <len(height)-1 else 0 for i in range(len(height))]
        for i in range(0,len(height)):
            l=l_mh[i]
            r=r_mh[i]
            if height[i]<min(l,r): 
                water=water+1*(min(l,r)-height[i])
        return water



            
            

        