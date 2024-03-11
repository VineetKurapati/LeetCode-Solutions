class Solution:
    def customSortString(self, order: str, s: str) -> str:
        pq = []
        d ={}
        i = 0
        for c in order:
            d[c] = i
            i+=1
        for ch in s:
            if ch not in d:
                heapq.heappush(pq, (i+1, ch))
                i+=1
            else:
                heapq.heappush(pq,(d[ch], ch))
        res = ""
        while pq:
            j, ch = heapq.heappop(pq)
            res += ch
        return res

