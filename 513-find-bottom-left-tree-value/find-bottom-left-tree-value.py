# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        left_most_value = None
        while queue:
            node = queue.popleft()
            left_most_value = node.val
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return left_most_value