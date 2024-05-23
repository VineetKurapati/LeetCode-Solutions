# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        depth = 1
        def dfs(root, depth):
            nonlocal res
            if not root:
                return
            if depth > len(res):
                res.append(root.val)
            depth +=1 
            dfs(root.right, depth)
            dfs(root.left, depth)
        dfs(root, depth)
        return res