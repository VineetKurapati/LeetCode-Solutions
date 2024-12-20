class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traversalDFS(left_root, right_root, level):
            if not left_root or not right_root:
                return 
            if level % 2 == 0:
                temp = left_root.val
                left_root.val = right_root.val
                right_root.val = temp 
            traversalDFS(left_root.left, right_root.right, level + 1)        
            traversalDFS(left_root.right, right_root.left, level + 1)
        traversalDFS(root.left, root.right, 0)
        return root