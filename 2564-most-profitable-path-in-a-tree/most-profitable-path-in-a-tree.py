class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        parent = [-1] * n
        depth = [0] * n
        
        def dfs(u: int, p: int):
            parent[u] = p
            for v in graph[u]:
                if v == p:
                    continue
                depth[v] = depth[u] + 1
                dfs(v, u)
        
        dfs(0, -1)
        bob_time = [inf] * n
        t = 0
        cur = bob
        while cur != -1:
            bob_time[cur] = t
            cur = parent[cur]
            t += 1
        res = -inf
        
        def dfs_alice(u: int, d: int, curr_profit: int):
            nonlocal res
            if d < bob_time[u]:
                curr_profit += amount[u]
            elif d == bob_time[u]:
                curr_profit += amount[u] // 2
            if u != 0 and len(graph[u]) == 1:
                res = max(res, curr_profit)
            for v in graph[u]:
                if v == parent[u]:
                    continue
                dfs_alice(v, d + 1, curr_profit)
        
        dfs_alice(0, 0, 0)
        return res
