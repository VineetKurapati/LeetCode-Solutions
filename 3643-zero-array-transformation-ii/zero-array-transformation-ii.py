from typing import List

class Solution:
    def isGood(self, target, n, queries, nums):
        diff = [0] * (n + 1)
        for l, r, val in queries[:target]:
            diff[l] += val
            if r + 1 < n:
                diff[r + 1] -= val
        
        curr = 0
        for i in range(n):
            curr += diff[i]
            if nums[i] > curr:
                return False  
        
        return True

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        q = len(queries)
        l, r = 0, q + 1 
        
        while l < r:
            m = (l + r) // 2
            if self.isGood(m, n, queries, nums):
                r = m  
            else:
                l = m + 1 
        
        return -1 if l > q else l  
