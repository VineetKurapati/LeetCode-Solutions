from collections import defaultdict
import heapq

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        indegree = defaultdict(int)
        
        # Calculate indegree for each node
        for u, v in roads:
            indegree[u] += 1
            indegree[v] += 1
        
        # Use a max heap to assign importance efficiently
        max_heap = [(-deg, node) for node, deg in indegree.items()]
        heapq.heapify(max_heap)
        
        importance = {}
        current_importance = n
        
        while max_heap:
            _, node = heapq.heappop(max_heap)
            importance[node] = current_importance
            current_importance -= 1
        
        # Calculate the total importance
        res = 0
        for u, v in roads:
            res += importance[u] + importance[v]
        
        return res
