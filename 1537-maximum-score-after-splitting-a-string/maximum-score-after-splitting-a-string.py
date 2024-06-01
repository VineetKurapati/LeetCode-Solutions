class Solution:
    def maxScore(self, s: str) -> int:
        max_score = float("-inf")
        
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            curr_score = left.count('0') + right.count('1')
            max_score = max(max_score, curr_score)
        
        return max_score
