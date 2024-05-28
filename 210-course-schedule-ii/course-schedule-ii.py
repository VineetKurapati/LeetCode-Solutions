class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = {i : 0 for i in range(n)}
        print(indegree)
        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        queue = deque()
        for i in indegree:
            if indegree[i] == 0:
                queue.append(i)
        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for neigh in adj[curr]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        if len(res) == n:
            return res
        else:
            return []
        


