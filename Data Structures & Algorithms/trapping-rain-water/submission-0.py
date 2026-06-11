class Solution:
    def trap(self, height: List[int]) -> int:
        water=0
        for i in range(0,len(height)):
                l_mh=max(height[:i]) if i>0 else 0
                r_mh=max(height[i+1:]) if i<len(height)-1 else 0
                if height[i]<min(l_mh,r_mh): 
                    water=water+1*(min(l_mh,r_mh)-height[i])
        return water



            
            

        