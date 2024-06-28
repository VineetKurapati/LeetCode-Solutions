class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        indegree = {}
        for u, v in roads:
            if u not in indegree:
                indegree[u] = 0
            if v not in indegree:
                indegree[v] = 0
            indegree[u] += 1
            indegree[v] += 1 
        indegree = sorted(indegree.items(), key=lambda x: x[1], reverse = True)
        importance = {}
        print(indegree)
        i = 0
        while i < len(indegree):
            importance[indegree[i][0]] = n
            n-=1
            i+=1
        res = 0
        for u, y in roads:
            res += importance[u] + importance[y]
        return res
        return 0