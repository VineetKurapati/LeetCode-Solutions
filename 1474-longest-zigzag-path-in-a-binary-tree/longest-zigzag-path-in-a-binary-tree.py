# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        if not root:
            return 0
        def dfs(root, left, count):
            nonlocal res 
            if not root:
                res = max(res, count)
                return 
            # we have a few choices to make here 
            if left:
                dfs(root.right, False, count + 1)
                dfs(root.left, True, 0)
            else:
                dfs(root.left, True, count + 1)
                dfs(root.right, False, 0)
            # we can start fresh from a node as well
            
           
        dfs(root.left, True, 0)
        dfs(root.right, False, 0)
        return res