class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        increasing = 1
        curr_length = 1

        for i in range(1, n):
            if nums[i-1] < nums[i]:
                curr_length += 1
            else:
                increasing = max(increasing, curr_length)
                curr_length = 1
        increasing = max(increasing, curr_length)
        decreasing = 0 
        curr_length = 1 
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                curr_length += 1
            else:
                decreasing = max(decreasing, curr_length)
                curr_length = 1
        decreasing = max(decreasing, curr_length)
        return max(decreasing, increasing)
