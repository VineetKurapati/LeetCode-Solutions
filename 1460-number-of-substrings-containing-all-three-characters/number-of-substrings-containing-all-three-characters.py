class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = { 'a': 0, 'b': 0, 'c': 0 }
        l, res = 0, 0
        
        for r in range(len(s)):
            count[s[r]] += 1

            while all(count[c] > 0 for c in 'abc'): 
                res += len(s) - r 
                count[s[l]] -= 1
                l += 1
        
        return res
