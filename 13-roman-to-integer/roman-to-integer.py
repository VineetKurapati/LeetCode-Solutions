class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V":5 , "X": 10, "L":50, "C":100, "D":500, "M":1000}
        count = 0
        n = len(s)
        i = 0
        while i < n - 1:
            if d[s[i]] < d[s[i+1]]:
                count += d[s[i+1]] - d[s[i]]
                i+=2
            else:
                count += d[s[i]]
                i+=1
        if i <= n-1:
            count += d[s[n-1]]
        return count