from collections import deque, defaultdict
from typing import List

class Solution:
    def runBFS(self, i, adj):
        queue = deque([i])
        vis = set()
        temp = []
        while queue:
            curr_node = queue.pop()  # Use popleft for BFS
            if curr_node in vis:
                continue
            vis.add(curr_node)
            if curr_node != i:
                temp.append(curr_node)
            for neigh in adj[curr_node]:
                queue.append(neigh)
        return sorted(temp)  # Sort the result as the problem might expect sorted order

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[v].append(u)  # Reverse the edge direction for finding ancestors

        res = []
        for i in range(n):
            temp = self.runBFS(i, adj)
            res.append(temp)
        return res
