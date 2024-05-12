class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        workers = []
        for i in range(n):
            workers.append((wage[i] / quality[i], quality[i])) 
        workers.sort()  
        
        pq = []  
        quality_sum = 0 
        min_cost = float('inf') 
        
        for ratio, q in workers:
            quality_sum += q
            heapq.heappush(pq, -q)
            if len(pq) > k: 
                quality_sum += heapq.heappop(pq)
            if len(pq) == k: 
                min_cost = min(min_cost, ratio * quality_sum)
        
        return min_cost
