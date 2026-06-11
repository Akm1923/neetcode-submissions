class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m={}
        left=0
        ans=0
        for right,ch in enumerate(s):
            if ch not in m:
                m[ch]=1
            else:
                m[ch]+=1
            max_freq=max(m.values())
            while (right-left +1)-max_freq >k:
                m[s[left]]-=1
                left=left+1
            ans=max(ans,right-left+1)
        return ans
            




        