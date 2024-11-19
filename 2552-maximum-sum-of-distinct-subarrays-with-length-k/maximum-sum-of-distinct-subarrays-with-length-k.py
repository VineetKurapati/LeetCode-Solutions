from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        current_sum = 0
        vis = set() 
        l = 0 
        
        for r in range(n): 
            while nums[r] in vis: 
                vis.remove(nums[l])
                current_sum -= nums[l]
                l += 1
            
            vis.add(nums[r])
            current_sum += nums[r]
            if r - l + 1 == k:
                res = max(res, current_sum)
                vis.remove(nums[l])
                current_sum -= nums[l]
                l += 1
                
        return res
