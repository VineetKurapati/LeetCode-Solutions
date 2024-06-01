import heapq
from typing import List

class KthLargest:

    def __init__(self, n: int, nums: List[int]):
        self.pq = []
        self.k = n
        for num in nums:
            self.add(num)
    
    def add(self, val: int) -> int:
        if len(self.pq) < self.k:
            heapq.heappush(self.pq, val)
        elif val > self.pq[0]:
            heapq.heapreplace(self.pq, val)
        
        return self.pq[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
