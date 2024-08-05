class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        m = Counter(arr)
        pq = []
        for i in range(len(arr)):
            c = arr[i]
            if m[c] == 1:
                heapq.heappush(pq, (i,c))
        res = ""
        if k > len(pq):
            return res
        while k and pq:
            i, c = heapq.heappop(pq)
            res = c
            k-=1
        return res
