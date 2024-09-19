from typing import List
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        vis = defaultdict(int)
        
        def backtrack(index, current_sum):
            if (index, current_sum) in vis:
                return vis[(index, current_sum)]
            if index == len(nums):
                if current_sum == target:
                    return 1
                else:
                    return 0
            add_ways = backtrack(index + 1, current_sum + nums[index])
            sub_ways = backtrack(index + 1, current_sum - nums[index])
            vis[(index, current_sum)] = add_ways + sub_ways
            
            return vis[(index, current_sum)]
        
        return backtrack(0, 0)
