class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        
        level_sum = {}
        
        def dfs(level, node):
            if not node:
                return
            if level not in level_sum:
                level_sum[level] = 0
            level_sum[level] += node.val
            dfs(level + 1, node.left)
            dfs(level + 1, node.right)
        dfs(0, root)
        max_heap = [-s for s in level_sum.values()] 
        heapq.heapify(max_heap)  
        if len(max_heap) < k:
            return -1
        for _ in range(k):
            if max_heap:  
                res = -heapq.heappop(max_heap)  
                
        return res if 'res' in locals() else 0  
