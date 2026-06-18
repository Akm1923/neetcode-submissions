# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = 0

    def goodNodes(self, root: TreeNode, m=None) -> int:

        if not root:
            return self.ans

        if m is None:
            m = root.val

        if root.val >= m:
            self.ans += 1

        m = max(m, root.val)

        self.goodNodes(root.left, m)
        self.goodNodes(root.right, m)

        return self.ans