class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        res = []
        for i in range(n):
            heap = []
            for j in range(i+ 1, n):
                if prices[j] <= prices[i]:
                    heapq.heappush(heap, (j, prices[j]))
            if heap:
                index, cost = heapq.heappop(heap)
                res.append(prices[i] - cost)
            else:
                res.append(prices[i])
        return res
