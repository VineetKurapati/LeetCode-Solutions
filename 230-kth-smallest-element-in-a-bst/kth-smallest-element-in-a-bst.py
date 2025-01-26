# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pq = []
        def dfs(root):
            nonlocal pq
            if not root:
                return 
            heapq.heappush(pq,  root.val)
            dfs(root.left)
            dfs(root.right)
        res = []
        dfs(root)
        temp = k
        while k:
            curr = heapq.heappop(pq)
            res.append(curr)
            k-=1 
        return res[temp - 1]