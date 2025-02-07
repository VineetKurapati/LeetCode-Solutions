class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        score = 0
        while heap and k:
            curr = -1 * heapq.heappop(heap)
            score += curr 
            val = ceil(curr/3)
            heapq.heappush(heap, -1 * val)
            k-=1
        return score