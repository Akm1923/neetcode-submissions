from typing import List

class Solution:
    def backtrack(self, idx, balance, s):
        if idx >= len(s):
            if balance == 0:
                self.res.append("".join(s))
            return

        # Invalid state
        if balance < 0 or balance > len(s) // 2:
            return

        # Place '('
        s[idx] = '('
        self.backtrack(idx + 1, balance + 1, s)

        # Place ')' only if there is an unmatched '('
        if balance > 0:
            s[idx] = ')'
            self.backtrack(idx + 1, balance - 1, s)

    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        s = [""] * (2 * n)
        self.backtrack(0, 0, s)
        return self.res