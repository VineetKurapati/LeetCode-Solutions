class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.dp = {}
        def dfs(i, count):
            if i >= len(nums) and count != target:
                return 0
            if i == len(nums) and count == target:
                return 1
            if (count, i) in self.dp:
                return self.dp[(count, i)]
            self.dp[(count, i)] = dfs(i + 1, count + nums[i]) + dfs(i + 1, count - nums[i])
            return self.dp[(count, i)]
        return dfs(0,0)