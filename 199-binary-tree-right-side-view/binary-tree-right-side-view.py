# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        def dfs(node, level):
            nonlocal res
            if not node:
                return 
            if level > len(res):
                res.append(node.val)
            level +=1 
            dfs(node.right, level)
            dfs(node.left, level)
        dfs(root, 1)
        return res