# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0 
        def search(root, left, count):
            nonlocal res
            if not root:
                return 
            res = max(res, count)
            if left:
                search(root.left, False, count+1)
                search(root.right, True, 1)
            else:
                search(root.right, True, count+1)
                search(root.left, False, 1)
            return
        search(root, True, 0)
        search(root, False, 0)
        return res