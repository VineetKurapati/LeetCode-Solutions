# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        s = 0
        def dfs(root, temp):
            nonlocal s
            if not root:
                return
            if not root.left and not root.right:
                s += (temp*10) + root.val
                return 
            temp = (temp * 10) + root.val
            dfs(root.left, temp)
            dfs(root.right, temp)
        dfs(root, 0)
        return s