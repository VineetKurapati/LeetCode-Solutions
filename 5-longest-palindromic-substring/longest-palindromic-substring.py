class Solution:
    def longestPalindrome(self, s: str) -> str:
        def search(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -=1
                j +=1 
            return s[i+1 : j]
        res = ""
        for i in range(len(s)):
            s1 = search(i,i)
            s2 = search(i, i + 1)
            if len(s1) >= len(res):
                res = s1
            if len(s2) >= len(res):
                res = s2
        return res