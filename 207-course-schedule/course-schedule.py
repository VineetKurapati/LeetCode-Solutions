class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        res = []
        for p in prerequisites:
            course = p[0]
            pre = p[1]
            adj[pre].append(course)
            indegree[course] += 1
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for neigh in adj[curr]:
                indegree[neigh] -=1 
                if indegree[neigh] == 0:
                    queue.append(neigh)
        return len(res) == n
