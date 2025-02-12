class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        n = len(s)
        for i in range(n):
            l, r = i, i
            while l >=0 and r < n and s[l] == s[r]:
                l -= 1 
                r +=1 
            if len(res) <= len(s[l + 1: r]):
                res = s[l + 1: r]
            l, r = i, i+1
            while l >=0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if len(res) <= len(s[l + 1: r]):
                res = s[l + 1: r]
        return res
