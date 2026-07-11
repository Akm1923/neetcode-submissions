from typing import List

class Solution:
    def dfs(self, board, word, i, j, idx):
        # Word completely matched
        if idx == len(word):
            return True

        # Boundary + Character check
        if (i < 0 or i >= len(board) or
            j < 0 or j >= len(board[0]) or
            board[i][j] != word[idx]):
            return False

        # Mark current cell as visited
        temp = board[i][j]
        board[i][j] = '#'

        # Explore 4 directions
        found = (
            self.dfs(board, word, i + 1, j, idx + 1) or
            self.dfs(board, word, i - 1, j, idx + 1) or
            self.dfs(board, word, i, j + 1, idx + 1) or
            self.dfs(board, word, i, j - 1, idx + 1)
        )

        # Backtrack (restore the cell)
        board[i][j] = temp

        return found

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                if self.dfs(board, word, i, j, 0):
                    return True

        return False