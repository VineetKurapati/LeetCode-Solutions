from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {}
        res = []
        
        # Count occurrences of each number in nums1
        for num in nums1:
            if num not in m:
                m[num] = 0
            m[num] += 1
        
        # For each number in nums2, if it exists in the map and count is not zero, 
        # append it to result and decrease the count
        for num in nums2:
            if num in m and m[num] > 0:
                res.append(num)
                m[num] -= 1
        
        return res
