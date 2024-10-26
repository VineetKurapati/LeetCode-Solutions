class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        left_sum = 0
        m = {}
        right_sum = sum(nums)
        for i in range(n):
            left_sum += nums[i]
            right_sum -= nums[i]
            left_diff = math.floor(left_sum / (i + 1))
            right_diff = math.floor(right_sum / (n - i - 1)) if (n - i -1 ) > 0 else 0
            avg_diff = abs(left_diff - right_diff)
            if avg_diff not in m:
                m[avg_diff] = float("inf")
            m[avg_diff] = min(m[avg_diff], i)
        mi = min(m)
        return m[mi]
            