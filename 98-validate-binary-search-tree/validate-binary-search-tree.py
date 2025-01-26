# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def search(root, min_val, max_val):
            if not root:
                return True 
            if root.val <= min_val or root.val >= max_val:
                return False 
            return search(root.left, min_val, min(max_val, root.val)) and search(root.right, max(root.val, min_val), max_val)
        return search(root, float("-inf"), float("inf"))