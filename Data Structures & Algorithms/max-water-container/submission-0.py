class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        m_vol=0
        while i<j:
            vol=(j-i)*min(heights[j],heights[i])
            if heights[j]>heights[i]:
                i=i+1
            elif heights[j]<=heights[i]:
                j=j-1
            m_vol=max(m_vol,vol)
        return m_vol

        