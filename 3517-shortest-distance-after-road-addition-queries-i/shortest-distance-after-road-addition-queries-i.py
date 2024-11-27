class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        def distance(adj_list, n):
            count = float("inf")
            queue = deque()
            queue.append((0, 0))
            vis = set()
            while queue:
                curr_node, curr_count = queue.popleft()
                if curr_node == n-1:
                    count = min(curr_count, count)
                for j in adj_list[curr_node]:
                    if j not in vis:
                        queue.append((j, curr_count + 1))
                        vis.add(j)
            return count
        for i in range(1, n):
            adj_list[i-1].append(i)
        res = []
        for s, e in queries:
            adj_list[s].append(e)
            res.append(distance(adj_list, n))
        return res
        