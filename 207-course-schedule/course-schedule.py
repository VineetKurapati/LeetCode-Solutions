class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        res = []
        while queue:
            curr = queue.pop()
            res.append(curr)
            for neigh in adj[curr]:
                indegree[neigh] -=1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        return len(res) == n