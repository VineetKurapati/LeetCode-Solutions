# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(root, target):
            if root is None:
                return
            if root.left is not None and root.left.val == target and root.left.left is None and root.left.right is None:
                root.left = None
            if root.right is not None and root.right.val == target and root.right.left is None and root.right.right is None:
                root.right = None
            dfs(root.left, target)
            dfs(root.right, target)
        def check(root, target):
            # Function to check if target is leaf node
            if root is None:
                return False
            if root.val == target and root.left is None and root.right is None:
                return True
            return check(root.left, target) or check(root.right, target)
        c = True
        while c:
            dfs(root, target)
            c = check(root, target)
            if root.left is None and root.right is None and root.val == target:
                return None
        return root