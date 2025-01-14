class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for f, t, p in flights:
            graph[f].append((t, p))
        queue = [(0, src, 0)]
        visited = defaultdict(lambda: float('inf'))
        
        while queue:
            price, curr_city, stops = heappop(queue)
            if curr_city == dst:
                return price
            if stops > k:
                continue
            for neighbor, cost in graph[curr_city]:
                new_price = price + cost
                if new_price < visited[(neighbor, stops)]:
                    visited[(neighbor, stops)] = new_price
                    heappush(queue, (new_price, neighbor, stops + 1))
        return -1
