from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Step 1: Use a dictionary to store the maximum beauty for each price
        d = {}
        for price, beauty in items:
            if price not in d:
                d[price] = 0
            d[price] = max(d[price], beauty)
        
        # Step 2: Convert the dictionary to a sorted list by price
        new_items = sorted(d.items())  # Each entry is [price, max_beauty]
        
        # Step 3: Accumulate maximum beauty up to each price for efficient querying
        for i in range(1, len(new_items)):
            new_items[i] = (new_items[i][0], max(new_items[i][1], new_items[i-1][1]))
        
        # Step 4: Answer each query using binary search
        res = []
        for q in queries:
            # Binary search to find the highest price <= q
            start, end = 0, len(new_items) - 1
            curr = 0  # Default beauty if no valid item found
            while start <= end:
                mid = start + (end - start) // 2
                if new_items[mid][0] <= q:
                    curr = new_items[mid][1]
                    start = mid + 1
                else:
                    end = mid - 1
            res.append(curr)
        
        return res
