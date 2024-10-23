from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = defaultdict(list)
        for (s, d), v in zip(equations, values):
            adj_list[s].append((d, v))
            adj_list[d].append((s, 1 / v))  # Add reverse edge

        def dfs(src, dest, val, visited):
            if src == dest:
                return val
            visited.add(src)
            for neighbor, v in adj_list[src]:
                if neighbor not in visited:
                    res = dfs(neighbor, dest, val * v, visited)
                    if res != -1:
                        return res
            return -1

        res = []
        for src, dest in queries:
            if src not in adj_list or dest not in adj_list:
                res.append(-1.0)
            elif src == dest:
                res.append(1.0)
            else:
                res.append(dfs(src, dest, 1.0, set()))
        
        return res
