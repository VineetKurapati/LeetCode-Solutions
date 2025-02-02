class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, curr):
            if i == len(nums) and curr == target:
                return 1
            if i>= len(nums) and curr != target:
                return 0
            if (i, curr) in dp:
                return dp[(i, curr)]
            minus = dfs(i + 1, curr - nums[i])
            plus = dfs(i + 1, curr + nums[i])
            dp[(i, curr)] = minus + plus 
            return dp[(i, curr)]
        return dfs(0, 0)