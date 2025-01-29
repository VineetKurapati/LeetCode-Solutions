from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]  
        rank = [1 for _ in range(n+1)]    

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  
            return parent[x]

        for u, v in edges:
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v: 
                return [u, v]
            if rank[root_u] >= rank[root_v]:
                parent[root_v] = root_u
                rank[root_u] += 1
            else:
                parent[root_u] = root_v
                rank[root_v] += 1
