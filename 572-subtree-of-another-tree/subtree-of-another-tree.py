# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root1, root2):
        if root1 and not root2:
            return False
        if not root1 and not root2:
            return True
        if not root1 and root2:
            return False
        if root1.val != root2.val:
            return False
        return self.check(root1.left, root2.left) and self.check(root1.right, root2.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root and subRoot:
            return False
        if root.val == subRoot.val and self.check(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
