from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        res = n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            nonlocal res
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_y] = root_x
                res -= 1
        
        for i in range(n):
            for j in range(i+1, n):  # Optimization: Only iterate over the upper triangular part since the matrix is symmetric
                if isConnected[i][j] == 1:
                    union(i, j)
        
        return res
