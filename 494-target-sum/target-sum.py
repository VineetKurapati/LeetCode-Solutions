class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(curr, i):
            nonlocal dp
            if i == len(nums) and curr == target:
                return 1
            if i >=len(nums) and curr != target:
                return 0
            if (curr, i) in dp:
                return dp[(curr, i)]
            dp[(curr, i)] = dfs(curr + nums[i], i + 1) + dfs(curr - nums[i], i + 1)
            return dp[(curr, i)]
        return dfs(0, 0)