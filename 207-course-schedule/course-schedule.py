class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        vis = set()
        processed = set()
        def search(curr_course):
            if curr_course in vis:
                return False 
            if curr_course in processed:
                return True 
            vis.add(curr_course)
            for neigh in graph[curr_course]:
                if not search(neigh):
                    return False 
            vis.remove(curr_course)
            processed.add(curr_course)
            return True 
        for i in range(numCourses):
            if not search(i):
                return False 
        return True
