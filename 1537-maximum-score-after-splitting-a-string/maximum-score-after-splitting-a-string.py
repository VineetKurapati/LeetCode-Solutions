class Solution:
    def maxScore(self, s: str) -> int:
        left_sum = []
        right_sum = []
        left = 0 
        n = len(s)
        for i in s:
            if i == "0":
                left += 1
            left_sum.append(left)
        right = 0
        for i in range(len(s) -1 , -1, -1):
            if s[i] == "1":
                right += 1
            right_sum.append(right)
        right_sum.reverse()
        res = 0
        print(left_sum)
        print(right_sum)
        for i in range(1, n):
            res = max(res, left_sum[i-1] + right_sum[i])
        return res