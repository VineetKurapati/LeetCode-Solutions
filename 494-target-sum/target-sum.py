class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.dp = {}
        def dfs(count, i):
            if i == len(nums) and count == target:
                return 1 
            if i >= len(nums) and count != target:
                return 0
            if (count, i) in self.dp:
                return self.dp[(count, i)]
            self.dp[(count, i)] = dfs(count + nums[i], i + 1) + dfs(count - nums[i], i + 1)
            return self.dp[(count, i)]
        return dfs(0,0)