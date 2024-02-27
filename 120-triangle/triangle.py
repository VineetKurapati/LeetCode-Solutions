class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp1 = [triangle[0][0]]
        for d in range(1, len(triangle)):
            dp1 = [
                min(
                    dp1[i] if i < len(dp1) else float("Inf"),
                    dp1[i - 1] if i > 0 else float("Inf"),
                )
                + v
                for i, v in enumerate(triangle[d])
            ]
        return min(dp1)