# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans=True
        def depth(root):
            if not root:
                return True
            left=depth(root.left)
            right=depth(root.right)
            diff=abs(left-right)
            if diff>1:
                self.ans=False
            return 1+max(left,right)
        depth(root)
        return self.ans    