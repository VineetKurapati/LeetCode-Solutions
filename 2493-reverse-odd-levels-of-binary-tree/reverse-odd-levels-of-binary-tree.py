# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverseDFS(root.left, root.right, 0)
        return root
    def traverseDFS(self, left_child, right_child, level):
        if left_child is None or right_child is None:
            return 
        if level % 2 == 0:
            temp = left_child.val
            left_child.val = right_child.val
            right_child.val = temp 
        self.traverseDFS(left_child.left, right_child.right, level + 1)
        self.traverseDFS(left_child.right, right_child.left, level + 1)