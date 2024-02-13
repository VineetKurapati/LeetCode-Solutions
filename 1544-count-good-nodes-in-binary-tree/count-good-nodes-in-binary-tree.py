# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 0
    
    def dfs(self, root, curr_val):
        if not root:
            return
        if root.val >= curr_val:
            self.count += 1
            curr_val = max(curr_val, root.val)
        self.dfs(root.left, curr_val)
        self.dfs(root.right, curr_val)
        
    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, float('-inf'))
        return self.count
