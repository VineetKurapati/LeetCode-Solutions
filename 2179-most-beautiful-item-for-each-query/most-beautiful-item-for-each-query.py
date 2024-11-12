class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        d = {}
        for price, beauty in items:
            if price not in d:
                d[price] = 0
            d[price] = max(d[price], beauty)
        new_items = sorted(d.items()) 
        for i in range(1, len(new_items)):
            new_items[i] = (new_items[i][0], max(new_items[i][1], new_items[i-1][1]))
        res = []
        for q in queries:
            start, end = 0, len(new_items) - 1
            curr = 0 
            while start <= end:
                mid = start + (end - start) // 2
                if new_items[mid][0] <= q:
                    curr = new_items[mid][1]
                    start = mid + 1
                else:
                    end = mid - 1
            res.append(curr)
        
        return res
