class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for e in edges:
            u = e[0]
            v = e[1]
            graph[u].append(v)
            graph[v].append(u)
        q = []
        q.append(source)
        vis = set()
        while q:
            curr = q.pop()
            if curr == destination:
                return True
            if curr in vis:
                continue
            vis.add(curr)
            for neigh in graph[curr]:
                q.append(neigh)
        return False