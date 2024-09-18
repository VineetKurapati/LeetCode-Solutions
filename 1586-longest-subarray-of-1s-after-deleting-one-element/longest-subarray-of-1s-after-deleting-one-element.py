class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0 
        count_zero = 0
        res = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count_zero +=1 
            while count_zero > 1:
                if nums[left] == 0:
                    count_zero -=1
                left += 1
            res = max(res, (right - left))
        return res