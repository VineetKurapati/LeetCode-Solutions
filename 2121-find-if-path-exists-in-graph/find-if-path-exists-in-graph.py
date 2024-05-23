class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parents = [x for x in range(n)]
        def union(x, y):
            x_p = find(x)
            y_p = find(y)
            if x_p != y_p:
                if x_p > y_p:
                    parents[x_p] = y_p
                elif y_p > x_p:
                    parents[y_p] = x_p
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        for u, v in edges:
            union(u,v)
        return find(source) == find(destination)