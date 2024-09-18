class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        num_zeroes = 0
        res = 0
        if k == 0 and sum(nums) == 0:
            return 0
        for right in range(len(nums)):
            if nums[right] == 0:
                num_zeroes +=1 
            while num_zeroes > k:
                if nums[left] == 0:
                    num_zeroes -=1
                left +=1 
            res = max(res, (right - left))
        return res + 1