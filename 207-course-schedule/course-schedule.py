class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        vis = set()
        graph = defaultdict(list)
        for pre in prerequisites:
            ai = pre[0]
            bi = pre[1]
            if ai not in graph:
                graph[ai] = []
            graph[ai].append(bi)
        def dfs(node):
            if node in vis:
                return False
            if graph[node] == []:
                return True
            vis.add(node)
            for n in graph[node]:
                if not dfs(n):
                    return False
            vis.remove(node)
            graph[node] = []
            return True
        for node in range(numCourses):
            if not dfs(node):
                return False
        return True