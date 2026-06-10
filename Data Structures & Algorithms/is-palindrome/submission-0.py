class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=""
        for ch in s:
            if ch.isalnum():
                l=l+ch.lower()
                
        l2="".join(reversed(l))
        return l==l2
        
        