from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        d = {}  # Dictionary to track element counts
        res = []  # Result array
        count = 0  # Common prefix count
        
        for a, b in zip(A, B):
            # Increment count in dictionary for both `a` and `b`
            if a in d:
                d[a] += 1
            else:
                d[a] = 1
            
            if b in d:
                d[b] += 1
            else:
                d[b] = 1
            
            # If an element's count reaches 2, it means it's common in both prefixes
            if d[a] == 2:
                count += 1
            if d[b] == 2 and a != b:  # Avoid double-counting if `a == b`
                count += 1
            
            res.append(count)  # Append current count to the result
        
        return res
