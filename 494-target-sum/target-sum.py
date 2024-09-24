class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(nums, i, n, curr, target):
            nonlocal dp
            if i == n and curr == target:
                return 1
            
            if i >= n and curr != target:
                return 0
            
            if (curr, i) in dp:
                return dp[(curr, i)]
            dp[(curr, i)] = dfs(nums, i+1, n, curr + nums[i], target) +dfs(nums, i+1, n, curr - nums[i], target)
            return dp[(curr, i)]
        return dfs(nums, 0, len(nums), 0, target)
