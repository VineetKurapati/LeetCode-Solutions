# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        levels = {}
        res = []
        def dfs(root, level):
            nonlocal levels
            if not root:
                return 
            if level not in levels:
                levels[level] = float("-inf")
            levels[level] = max(levels[level], root.val)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        for l in levels:
            res.append(levels[l])
        return res