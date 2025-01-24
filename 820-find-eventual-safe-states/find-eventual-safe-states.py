class Solution:
    def eventualSafeNodes(self, g: List[List[int]]) -> List[int]:
        n = len(g)
        vis = {}
        for i in range(n):
            if g[i] == []:
                vis[i] = True
        res = []
        def isSafe(i):
            nonlocal vis
            if i in vis:
                return vis[i]
            vis[i] = False
            for neigh in g[i]:
                if not isSafe(neigh):
                    return False 
            vis[i] = True
            return True
        for i in range(n):
            if isSafe(i):
                res.append(i)
        return res