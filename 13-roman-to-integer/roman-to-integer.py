class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        d = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        i = 0
        while i  < len(s):
            if i + 1 < len(s) and d[s[i]] < d[s[i + 1]]:
                res += d[s[i+1]] - d[s[i]]
                i += 2
            else:
                res += d[s[i]]
                i += 1
        return res 