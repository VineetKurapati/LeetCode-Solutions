# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(root, level, temp):
            if not root:
                return
            if len(temp) == level and root:
                temp.append(root.val)
            bfs(root.right, level + 1, temp)
            bfs(root.left, level + 1, temp)
            return temp
        return bfs(root, 0, [])