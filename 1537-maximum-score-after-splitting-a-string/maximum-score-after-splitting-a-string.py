class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        left_sum = [0] * n
        right_sum = [0] * n
        
        # Compute left_sum
        count_zeros = 0
        for i in range(n):
            if s[i] == "0":
                count_zeros += 1
            left_sum[i] = count_zeros
        
        # Compute right_sum
        count_ones = 0
        for i in range(n - 1, -1, -1):
            if s[i] == "1":
                count_ones += 1
            right_sum[i] = count_ones
        
        # Calculate maximum score
        max_score = 0
        for i in range(1, n):  # Split at position i
            max_score = max(max_score, left_sum[i - 1] + right_sum[i])
        
        return max_score
