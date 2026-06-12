from collections import deque
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        
        for i in tokens:
            if i not in ("+", "-", "*", "/"):
                stack.append(i)
            else:
                e2 = stack.pop()
                e1 = stack.pop()

                if i == "/":
                    ans = str(int(eval(e1 + i + e2)))
                else:
                    ans = str(eval(e1 + i + e2))
                stack.append(ans)
        return int(stack[0])
