class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def search(i):
            if i >= len(nums):
                return 0
            if i in dp:
                return dp[i]
            rob_current = nums[i] + search(i + 2)
            rob_next = search(i + 1)
            dp[i] = max(rob_current, rob_next)
            return dp[i]
        return search(0)