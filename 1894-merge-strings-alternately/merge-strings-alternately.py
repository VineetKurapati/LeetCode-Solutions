class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        l, r = 0, 0 
        n, m = len(word1), len(word2)
        while l < n and r < m:
            res += word1[l]
            res += word2[r]
            l+=1
            r+=1 
        if l < n:
            while l < n:
                res += word1[l]
                l+=1
        if r < m:
            while r < m:
                res += word2[r]
                r += 1
        return res