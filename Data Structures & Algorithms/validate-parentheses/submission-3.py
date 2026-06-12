from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack=deque()
        d={')':'(','}':'{',']':'['}
        for i in s:
            if i in d.values():
                stack.append(i)
            elif i in d.keys():
                if len(stack)!=0 and d[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack)==0