class Solution:
    def checkRecord(self, s: str) -> bool:
        m = {}
        for c in s:
            if c not in m:
                m[c] = 0
            m[c] +=1
            if c == "A" and m[c] > 1:
                return False
        if len(s) >= 3:
            for i in range(2, len(s)):
                if s[i] == "L" and s[i-1] == "L" and s[i-2] == "L":
                    return False
        return True