# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, min_value, max_value):
            if not root:
                return True 
            if root.val <=min_value or root.val >= max_value:
                return False 
            return helper(root.left, min_value, min(max_value, root.val)) and helper(root.right, max(min_value, root.val), max_value)
        return helper(root, float("-inf"), float("inf"))