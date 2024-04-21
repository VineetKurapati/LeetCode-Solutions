class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        vis = set()
        queue = []
        queue.append(source)
        adj_list = defaultdict(list)
        for edge in edges:
            u, v = edge
            adj_list[u].append(v)
            adj_list[v].append(u)  
        while queue:
            curr = queue.pop()
            print(curr)
            if curr == destination:
                return True
            if curr in vis:
                continue
            vis.add(curr)
            for neigh in adj_list[curr]:
                queue.append(neigh)
        return False