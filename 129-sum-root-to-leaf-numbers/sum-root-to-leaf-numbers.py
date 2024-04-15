# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def get(root, temp):
            nonlocal res
            if root is None:
                return
            char = str(root.val)
            temp += char
            if root.left is None and root.right is None:
                res += int(temp)
                return
            get(root.left, temp )
            get(root.right, temp)
        get(root, "")
        return res