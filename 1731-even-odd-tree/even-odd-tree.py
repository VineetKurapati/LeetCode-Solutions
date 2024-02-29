from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        ans = True
        q = deque([root])
        level = 0

        while q:
            curr_len = len(q)
            prev_val = None

            for _ in range(curr_len):
                node = q.popleft()

                if node:
                    if level % 2 == 0:
                        if node.val % 2 == 0:
                            return False
                        if prev_val:
                            if node.val <= prev_val:
                                return False
                        if not prev_val:
                            prev_val = node.val
                        
                    if level % 2 != 0:
                        if node.val % 2 != 0:
                            return False
                        if prev_val:
                            if node.val >= prev_val:
                                return False
                        if not prev_val:
                            prev_val = node.val

                    prev_val = node.val

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    
            level+= 1

        return ans
                        
                            
                        