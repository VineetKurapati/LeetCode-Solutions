class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        def kadne_max(nums):
            count = nums[0]
            c = 0
            for i in nums:
                if c < 0:
                    c = 0 
                c += i
                count = max(c, count)
            return count 
        def kadne_min(nums):
            count = nums[0]
            c = 0 
            for i in nums:
                if c > 0:
                    c = 0
                c += i
                count = min(c, count)
            return count
        return max(abs(kadne_min(nums)), kadne_max(nums))
