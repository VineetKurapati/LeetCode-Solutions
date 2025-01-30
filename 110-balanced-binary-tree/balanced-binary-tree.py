class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def bal(root):
            if not root:
                return 0, True  

            left_height, left_balanced = bal(root.left)
            right_height, right_balanced = bal(root.right)
            if not left_balanced or not right_balanced or abs(left_height - right_height) > 1:
                return max(left_height, right_height) + 1, False

            return max(left_height, right_height) + 1, True

        return bal(root)[1]
