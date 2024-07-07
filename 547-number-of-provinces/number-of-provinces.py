class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = defaultdict(set)
        n = len(isConnected)
        count = 0 
        vis = set()
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    adj[i].add(j)
        def dfs(curr_node):
            for neigh in adj[curr_node]:
                if neigh not in vis:
                    vis.add(neigh)
                    dfs(neigh)
        for curr_node in adj:
            if curr_node not in vis:
                dfs(curr_node)
                count += 1
        return count