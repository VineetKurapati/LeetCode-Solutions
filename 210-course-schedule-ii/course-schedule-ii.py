class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
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



        