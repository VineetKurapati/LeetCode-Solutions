class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1 for _ in range(n + 1)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  
            return parent[x]
        for x, y in edges:
            X = find(x)
            Y = find(y) 
            if X == Y:
                return [x, y]
            if rank[X] > rank[Y]:
                parent[Y] = X
                rank[X] += 1
            else:
                parent[X] = Y
                rank[Y] +=1