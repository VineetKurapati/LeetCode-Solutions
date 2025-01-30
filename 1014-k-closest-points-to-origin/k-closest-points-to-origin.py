class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Use a min-heap to store points based on their distances
        pq = []
        
        # Calculate distance and push into the heap
        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(pq, (distance, [x, y]))  # Push tuple (distance, point)
        
        # Extract the k closest points
        res = []
        for _ in range(k):
            res.append(heapq.heappop(pq)[1])  # Get the point from the heap
        
        return res