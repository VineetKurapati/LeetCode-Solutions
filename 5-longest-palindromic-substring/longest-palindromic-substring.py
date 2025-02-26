class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def expandaroundcenter(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -=1 
                j+=1 
            return s[i + 1:j]
        res = ""
        for i in range(n):
            first = expandaroundcenter(i, i)
            second = expandaroundcenter(i, i + 1)
            if len(first) >= len(res):
                res = first
            if len(second) >= len(res):
                res = second 
        return res