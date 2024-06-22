from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = 1 if nums[i] % 2 != 0 else 0
        count = 0
        prefix_sum = 0
        prefix_counts = {0: 1}
        
        for num in nums:
            prefix_sum += num
            
            if prefix_sum - k in prefix_counts:
                count += prefix_counts[prefix_sum - k]
            
            if prefix_sum in prefix_counts:
                prefix_counts[prefix_sum] += 1
            else:
                prefix_counts[prefix_sum] = 1
        
        return count
