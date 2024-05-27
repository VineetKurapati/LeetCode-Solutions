class Solution:
    def specialArray(self, nums: List[int]) -> int:
        max_num = max(nums)
        dp = [0 for i in range(max_num + 1)]
        for num in nums:
            for i in range(0, num+1):
                dp[i] += 1
        for i in range(len(dp)):
            if dp[i] == i:
                return i
        return -1