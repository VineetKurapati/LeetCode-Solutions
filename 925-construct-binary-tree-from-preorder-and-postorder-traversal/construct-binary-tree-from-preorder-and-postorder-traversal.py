# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Pre Order -> Root -- Left -- Right 
        # Post Order -> Left -- Right -- Root
        if not preorder or not postorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        left_index = postorder.index(preorder[1]) + 1
        root.left = self.constructFromPrePost(preorder[1:left_index+1], postorder[:left_index])
        root.right = self.constructFromPrePost(preorder[left_index + 1: ], postorder[left_index:])
        return root
