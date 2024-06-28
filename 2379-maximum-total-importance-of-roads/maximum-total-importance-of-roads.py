class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        indegree = defaultdict(int)
        
        # Calculate indegree for each node
        for u, v in roads:
            indegree[u] += 1
            indegree[v] += 1
        
        # Sort nodes by their indegree in descending order
        sorted_nodes = sorted(indegree.keys(), key=lambda x: indegree[x], reverse=True)
        
        # Assign importance values
        importance = {}
        current_importance = n
        
        for node in sorted_nodes:
            importance[node] = current_importance
            current_importance -= 1
        
        # Calculate the total importance
        res = 0
        for u, v in roads:
            res += importance[u] + importance[v]
        
        return res
