# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        def dfs(root, temp):
            nonlocal res
            if root is None:
                return
            temp = temp * 10 + root.val
            if root.left is None and root.right is None:
                res += temp
                return
            dfs(root.left, temp)
            dfs(root.right, temp)
        dfs(root, 0)
        return res