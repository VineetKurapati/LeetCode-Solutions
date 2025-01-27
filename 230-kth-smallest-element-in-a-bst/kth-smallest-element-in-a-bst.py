# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.pq = []
        def helper(root):
            if not root:
                return 
            heapq.heappush(self.pq, root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        temp = []
        t = k 
        while t:
            curr = heapq.heappop(self.pq)
            temp.append(curr)
            t -= 1
        return temp[k-1]
