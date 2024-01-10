class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        l1 = [0] * n
        for i in range(n):
            l1[i] = i
        def get(x):
            return l1[x]
        def union(x, y):
            rx = get(x)
            ry = get(y)
            if(rx != ry):
               for i in range(0, len(l1)):
                   if l1[i] == ry:
                       l1[i] = rx
        for i in range(0, n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    union(i, j)
        return len(set(l1))