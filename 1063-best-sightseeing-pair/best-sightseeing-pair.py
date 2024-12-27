class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        # In the problem we have to basically maximize (values[i] + values[j] + (i-j))
        maxTillNow = float("-inf")
        res = 0
        for i in range(n):
            current_value = values[i] - i
            res = max(res, (maxTillNow + current_value))
            current_value = values[i] + i
            maxTillNow = max(current_value, maxTillNow)
        return res