# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        d = {}
        def bfs(root, level):
            if not root:
                return
            if level not in d:
                d[level] = 0
            d[level] += root.val
            bfs(root.left, level + 1)
            bfs(root.right, level + 1)
        bfs(root, 1)
        maxi = float("-inf")
        res = 0
        for l in d:
            if d[l] > maxi:
                maxi = d[l]
                res = l
        return res
